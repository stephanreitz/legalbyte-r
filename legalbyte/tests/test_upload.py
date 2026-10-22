# pytest provides the Django database marker used by this test.
import pytest
# SimpleUploadedFile creates an in-memory file without reading the local disk.
from django.core.files.uploadedfile import SimpleUploadedFile
# APIClient simulates HTTP requests to the Django REST Framework API.
from rest_framework.test import APIClient
# A real user is required to obtain the JWT used by the upload request.
from apps.users.models import User


# Allow this test to use pytest-django's isolated test database.
@pytest.mark.django_db
def test_authenticated_user_can_upload_spreadsheet():

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