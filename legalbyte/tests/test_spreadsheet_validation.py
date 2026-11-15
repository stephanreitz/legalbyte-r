# BytesIO represents a binary XLSX file stored in memory.
from io import BytesIO
# pytest provides access to the isolated test database.
import pytest
# SimpleUploadedFile simulates files submitted by the frontend.
from django.core.files.uploadedfile import SimpleUploadedFile
# Workbook creates structurally valid XLSX files for validation tests.
from openpyxl import Workbook
# APIClient simulates HTTP requests to the API.
from rest_framework.test import APIClient
# Request is used to confirm that invalid submissions are not persisted.
from apps.requests.models import Request
# User is required because the upload endpoint is protected.
from apps.users.models import User

def create_authenticated_client():
    # Create a user in the isolated test database.
    user = User.objects.create_user(
        email="user@example.com",
        password="secret123",
    )
    client = APIClient()
    # Authentication itself is already covered by dedicated JWT tests.
    client.force_authenticate(user=user)
    return client

def create_xlsx_upload(sheet_name, headers):
    # Create a valid XLSX workbook with the requested structure.
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = sheet_name
    worksheet.append(headers)
    content = BytesIO()
    workbook.save(content)
    workbook.close()
    return SimpleUploadedFile(
        "planilha.xlsx",
        content.getvalue(),
        content_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
    )

# Allow the test to query the isolated test database.
@pytest.mark.django_db
def test_rejects_file_that_is_not_a_valid_xlsx(settings, tmp_path):
    settings.MEDIA_ROOT = tmp_path
    client = create_authenticated_client()
    # The extension says XLSX, but the content is not a real workbook.
    invalid_file = SimpleUploadedFile(
        "planilha.xlsx",
        b"not-an-xlsx-file",
        content_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
    )
    response = client.post(
        "/api/requests/",
        {
            "input_file": invalid_file,
            "criteria": ["Licitação"],
            "sheet_name": "TRATADAS",
        },
        format="multipart",
    )
    assert response.status_code == 400
    assert Request.objects.count() == 0

# Allow the test to query the isolated test database.
@pytest.mark.django_db
def test_rejects_spreadsheet_without_treated_sheet(settings, tmp_path):
    settings.MEDIA_ROOT = tmp_path
    client = create_authenticated_client()
    spreadsheet = create_xlsx_upload(
        sheet_name="OUTRA ABA",
        headers=["Publicação"],
    )
    response = client.post(
        "/api/requests/",
        {
            "input_file": spreadsheet,
            "criteria": ["Licitação"],
            "sheet_name": "TRATADAS",
        },
        format="multipart",
    )
    assert response.status_code == 400
    assert Request.objects.count() == 0
    
# Allow the test to query the isolated test database.
@pytest.mark.django_db
def test_rejects_spreadsheet_without_publication_column(settings, tmp_path):
    settings.MEDIA_ROOT = tmp_path
    client = create_authenticated_client()
    spreadsheet = create_xlsx_upload(
        sheet_name="TRATADAS",
        headers=["Nº do Processo", "Data de Publicação"],
    )
    response = client.post(
        "/api/requests/",
        {
            "input_file": spreadsheet,
            "criteria": ["Licitação"],
            "sheet_name": "TRATADAS",
        },
        format="multipart",
    )
    assert response.status_code == 400
    assert Request.objects.count() == 0