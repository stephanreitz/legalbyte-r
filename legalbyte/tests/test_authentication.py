import pytest
from rest_framework.test import APIClient
from apps.users.models import User

@pytest.mark.django_db
def test_user_can_login_with_email_and_password():
    
    User.objects.create_user(
        email="user@example.com",
        password="secret123",
    )

    client = APIClient()

    response = client.post(
        "/api/token/",
        {
            "email": "user@example.com",
            "password": "secret123",
        },
        format="json",
    )


    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data



