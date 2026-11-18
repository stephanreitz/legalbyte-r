import pytest
from rest_framework.test import APIClient
from apps.users.models import User


@pytest.mark.django_db
def test_user_can_register():
    client = APIClient()

    response = client.post(
        "/api/users/",
        {
            "email": "user@example.com",
            "password": "secret123",
        },
        format="json",
    )

    assert response.status_code == 201

    # Confirm that registration persisted exactly one user.
    user = User.objects.get(email="user@example.com")

    # create_user must hash the password while preserving authentication.
    assert user.check_password("secret123")

    # The API must never expose the password in its response.
    assert "password" not in response.data