# timedelta represents the three-dau retention interval.
from datetime import timedelta

# pytest provides access to the isolated test database.
import pytest

# SimpleUploadFile creates physical test files through Django storage.
from django.core.files.uploadedfile import SimpleUploadedFile

# call_command executes a Django management command inside the test.
from django.core.management import call_command

# timezone provides timezone-aware dates compatible with Django.
from django.utils import timezone

# APIClient verifies download behavior after file deletion.
from rest_framework.test import APIClient

# Requests stores the file paths and creation timestamp.
from apps.requests.models import Request

# User owns the Requests used by the test.
from apps.users.models import User


@pytest.mark.django_db
def test_cleanup_removes_expired_files_but_keeps_request_metadata(settings, tmp_path):

    # Isolate files from the project's real media directory.
    settings.MEDIA_ROOT = tmp_path

    # Create a user in the isolated test database.
    user = User.objects.create_user(
        email="user@example.com",
        password="secret123",
    )

    # Create a Request that will be made older than the retention period.
    expired_request = Request.objects.create(
        user=user,
        input_file=SimpleUploadedFile(
            "expired-input.xlsx",
            b"expired-input-content",
        ),
        output_file=SimpleUploadedFile(
            "expired-output.xlsx",
            b"expired-output-content",
        ),
    )

    # Create a recent Request whose files must remain available.
    recent_request = Request.objects.create(
        user=user,
        input_file=SimpleUploadedFile(
            "recent-input.xlsx",
            b"recent-input-content",
        ),
        output_file=SimpleUploadedFile(
            "recent-output.xlsx",
            b"recent-output-content",
        ),
    )

    # auto_now_add cannot be passed to create(), so update it directly.
    Request.objects.filter(id=expired_request.id).update(
        created_at=timezone.now() - timedelta(days=4)
    )
    expired_request.refresh_from_db()

    # Preserve the database paths for comparison after cleanup.
    expired_input_name = expired_request.input_file.name
    expired_output_name = expired_request.output_file.name
    recent_input_name = recent_request.input_file.name
    recent_output_name = recent_request.output_file.name

    # Confirm that all four files exisist before cleanup.
    assert expired_request.input_file.storage.exists(expired_input_name)
    assert expired_request.output_file.storage.exists(expired_output_name)
    assert recent_request.input_file.storage.exists(recent_input_name)
    assert recent_request.output_file.storage.exists(recent_output_name)

    # Execute the retention operation as it would be run by a scheduler.
    call_command("cleanup_expired_request_files")
    expired_request.refresh_from_db()
    recent_request.refresh_from_db()

    # Both Request records must remain in the database.
    assert Request.objects.count() == 2

    # Historical paths mus remain stored as metadata.
    assert expired_request.input_file.name == expired_input_name
    assert expired_request.output_file.name == expired_output_name

    # Expired physical files must be deleted.
    assert not expired_request.input_file.storage.exists(expired_input_name)
    assert not expired_request.output_file.storage.exists(expired_output_name)

    # Recent physical files must remain available.
    assert recent_request.input_file.storage.exists(recent_input_name)
    assert recent_request.output_file.storage.exists(recent_output_name)

    # An expired output path must not produce an internal server error.
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get(
        f"/api/resquests/{expired_request.id}/download"
    )

    assert response.status_code == 404