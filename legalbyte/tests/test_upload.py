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

# BytesIO creates the XLSX inpout entirely in memory.
from io import BytesIO

# Workbook creates a valid XLSX file and load_workbook reads the result.
from openpyxl import Workbook, load_workbook

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

    # Create a valid input workbook using the spreadsheet contract.
    input_workbook = Workbook()
    input_sheet = input_workbook.active
    input_sheet.title = "TRATADAS"

    input_sheet.append([
        "Nº do Processo",
        "Data de Cadastro",
        "Data de Disponibilização",
        "Data de Publicação",
        "Publicação",    
    ])

    input_sheet.append([
        "0001",
        "01/01/2026",
        "02/01/2026",
        "03/01/2026",
        "Foi publicado um aviso de pregão eletrônico.",
    ])    

    # Serialize the workbook into binary XLSX content.
    input_content = BytesIO()
    input_workbook.save(input_content)
    uploaded_content = input_content.getvalue()
    input_workbook.close()

    spreadsheet = SimpleUploadedFile(
        "planilha.xlsx",
        uploaded_content,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    # This value simulates the sheet selected by the frontend.
    sheet_name = "TRATADAS"

    # These criteria simulate the values submitted by the frontend.
    criteria = [
        "Licitação",
        "Pregão eletrônico",
]

    # Send the file as multipart/form-data, the standard HTTP upload format.
    response = client.post(
        "/api/requests/",
        {"input_file": spreadsheet,
         "criteria": criteria,
         "sheet_name": sheet_name
         },
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
        assert stored_file.read() == uploaded_content

    # Confirm that the processing  parameters were stored with the Request
    assert created_request.criteria == criteria

    # Confirm that theselected sheet was stored with Request.
    assert created_request.sheet_name == sheet_name

    # Confirm that synchronous processing generated an output file.
    assert created_request.output_file.name.startswith("outputs/")
    assert created_request.output_file.name.endswith(".xlsx")

    # Confirm that the output was physically stored.
    assert created_request.output_file.storage.exists(
        created_request.output_file.name
    )

    # Open the generated output and verify its analysis.
    with created_request.output_file.open("rb") as stored_output:
        output_workbook = load_workbook(stored_output)
        output_sheet = output_workbook.active
        rows = list(output_sheet.iter_rows(values_only=True))

    assert rows[0][-2:] == (
        "Retorno robô",
        "Critério localizado",
    )

    assert rows[1][-2:] == (
        "Desconsiderar publicação",
        "Pregão eletrônico",
    )

    output_workbook.close()

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