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


@pytest.mark.django_db
def test_login_rejects_invalid_credentials():

    User.objects.create_user(
        email="user@example.com",
        password="secret123",
    )

    client = APIClient()

    response = client.post(
        "/api/token/",
        {
            "email": "user@example.com",
            "password": "wrong-password",
        },
        format="json",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_login_requires_email_and_password():

    client = APIClient()

    response = client.post("/api/token/", {}, format="json",)

    assert response.status_code == 400

@pytest.mark.django_db
def test_user_can_refresh_access_token():

    User.objects.create_user(
        email="user@example.com",
        password="secret123",
    )


    client = APIClient()

    login = client.post(
        "/api/token/",
        {
            "email": "user@example.com",
            "password": "secret123",
        },
        format="json",
    )
    refresh = login.data["refresh"]

    response = client.post(
        "/api/token/refresh/",
        {
            "refresh": refresh,
        },
        format="json",
    )

    assert response.status_code == 200
    assert "access" in response.data