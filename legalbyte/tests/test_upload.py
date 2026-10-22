# pytest provides the Django database marker used by this test.
import pytest
# SimpleUploadedFile creates an in-memory file without reading the local disk.
from django.core.files.uploadedfile import SimpleUploadedFile
# APIClient simulates HTTP requests to the Django REST Framework API.
from rest_framework.test import APIClient
# A real user is required to obtain the JWT used by the upload request.
from apps.users.models import User
# The Request model lets the test confirm that rejected uploads are not saved.
from apps.requests.models import Request

# Allow this test to use pytest-django's isolated test database.
@pytest.mark.django_db
def test_authenticated_user_can_upload_spreadsheet(settings, tmp_path):

    # Store test uploads in a isolated temporary directory.
    settings.MEDIA_ROOT = tmp_path

    # Create a user in the test database. create_user hashes the password.
    user = User.objects.create_user(
        email="user@example.com",
        password="secret123",
    )

    # Create an HTTP client that will act as the frontend in this test.
    client = APIClient()
    # Log in with the test user to obtain the JWT access and refresh tokens.
    login = client.post(
        "/api/token/",
        {"email": "user@example.com", "password": "secret123"},
        format="json",
    )
    # Add the access token to the Authorization header of subsequent requests.
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {login.data['access']}")

    # Build a fake spreadsheet in memory. Sprint 2 tests file transport and
    # storage, not whether the bytes form a valid XLSX workbook.
    spreadsheet = SimpleUploadedFile(
        "planilha.xlsx",
        b"fake-xlsx-content",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    # Send the file as multipart/form-data, the standard HTTP upload format.
    response = client.post(
        "/api/requests/",
        {"input_file": spreadsheet},
        format="multipart",
    )

    # HTTP 201 confirms that the API created a new Request resource.
    assert response.status_code == 201

    # Confirm that one Request was saved in the test database.
    created_request = Request.objects.get()

    # Confirm that the Request belongs to the authenticated user.
    assert created_request.user == user

    # Confirm that the database stores the relative file path.
    assert created_request.input_file.name == "uploads/planilha.xlsx"

    # Confirm that the file was physically saved by the configured storage.
    assert created_request.input_file.storage.exists(
        created_request.input_file.name
    )
    
    # Confirm that the stored file contains the uploaded bytes.
    with created_request.input_file.open("rb") as stored_file:
        assert stored_file.read() == b"fake-xlsx-content"

# Allow the test to query the isolated test database.
@pytest.mark.django_db
def test_unauthenticated_user_cannot_upload_spreadsheet():

    # This client does not receive a JWT Authorization header.
    client = APIClient()

    # Create an in-memory file to simulate an attempted upload.
    spreadsheet = SimpleUploadedFile(
        "planilha.xlsx",
        b"fake-xlsx-content",
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    # Attempt to upload without authenticating.
    response = client.post(
        "/api/requests/",
        {"input_file": spreadsheet},
        format="multipart",
    )

    # The API must reject anonymous users.
    assert response.status_code == 401

    # A rejected request must not create a database record.
    assert Request.objects.count() == 0

# Allow the test to create and query Requests in the isolated test database.
@pytest.mark.django_db
def test_authenticated_user_can_list_only_their_requests():

    # Create the user who will perform the request.
    user = User.objects.create_user(
        email="user@example.com",
        password="secret123",
    )

    # Create another user to verify data isolation.
    other_user = User.objects.create_user(
        email="other@example.com",
        password="secret123",
    )

    # Create one Request owned by the authenticated user.
    own_request = Request.objects.create(
        user=user,
        input_file="uploads/own.xlsx",
    )

    # Create another Request that must not appear in the response.
    Request.objects.create(
        user=other_user,
        input_file="uploads/other.xlsx",
    )

    # Create an HTTP client and obtain a JWT for the first user.
    client = APIClient()
    login = client.post(
        "/api/token/",
        {
            "email": "user@example.com",
            "password": "secret123",
        },
        format="json",
    )

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {login.data['access']}"
    )

    # Request the list of Requests belonging to the authenticated user.
    response = client.get("/api/requests/")

    # The endpoint must return the list successfully.
    assert response.status_code == 200

    # Only the authenticated user's Request must be returned.
    assert len(response.data) == 1
    assert response.data[0]["id"] == own_request.id