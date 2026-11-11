# pytest provides database access for the tests.
import pytest

# SimpleUploadedFile creates an output file without reading the local disk.
from django.core.files.uploadedfile import SimpleUploadedFile

# APIClient simulates requests to the API.
from rest_framework.test import APIClient

# Request represents the processed publication request.
from apps.requests.models import Request

# User is required to test ownership and authentication.
from apps.users.models import User

# Allow this test to use the isolated test database.
@pytest.mark.django_db
def test_user_can_download_own_output(settings, tmp_path):

    # Store test files outside the project's real media directory.
    settings.MEDIA_ROOT = tmp_path

    user = User.objects.create_user(
        email="user@example.com",
        password="secret123",
    )

    # Create a processed Request with an output file.
    publication_request = Request.objects.create(
        user=user,
        input_file="uploads/input.xlsx",
        output_file=SimpleUploadedFile(
            "analysis.xlsx",
            b"processed-xlsx-content",
        ),
    )

    client = APIClient()

    # Authenticate directly because JWT behavior is already tested separately.
    client.force_authenticate(user=user)

    response = client.get(
        f"/api/requests/{publication_request.id}/download/"
    )

    assert response.status_code == 200

    # The response must instruct the client to download the file.
    assert "attachment" in response["Content-Disposition"]

    # FileResponse streams the file instead of loading it all at once.
    downloaded_content = b"".join(response.streaming_content)
    assert downloaded_content == b"processed-xlsx-content"

# Allow this test to use the isolated test database.
@pytest.mark.django_db
def test_unauthenticated_user_cannot_download_output(settings, tmp_path):

    settings.MEDIA_ROOT = tmp_path

    owner = User.objects.create_user(
        email="owner@example.com",
        password="secret123",
    )

    publication_request = Request.objects.create(
        user=owner,
        input_file="uploads/input.xlsx",
        output_file=SimpleUploadedFile(
            "analysis.xlsx",
            b"processed-xlsx-content",
        ),
    )

    # This client has no authenticated user.
    client = APIClient()
    response = client.get(
        f"/api/requests/{publication_request.id}/download/"
    )

    assert response.status_code == 401

# Allow this test to use the isolated test database.
@pytest.mark.django_db
def test_user_cannot_download_another_users_output(settings, tmp_path):

    settings.MEDIA_ROOT = tmp_path

    owner = User.objects.create_user(
        email="owner@example.com",
        password="secret123",
    )

    other_user = User.objects.create_user(
        email="other@example.com",
        password="secret123",
    )

    publication_request = Request.objects.create(
        user=owner,
        input_file="uploads/input.xlsx",
        output_file=SimpleUploadedFile(
            "analysis.xlsx",
            b"processed-xlsx-content",
        ),
    )

    client = APIClient()

    client.force_authenticate(user=other_user)

    response = client.get(
        f"/api/requests/{publication_request.id}/download/"
    )
    
    # Return 404 instead of exposing that another user's Request exists.
    assert response.status_code == 404