import pytest
from apps.users.models import User

def test_user_uses_email_as_username_field():
    assert User.USERNAME_FIELD == "email"

def test_user_does_not_have_username_field():

    fields_names = [field.name for field in User._meta.get_fields()]

    assert "username" not in fields_names

@pytest.mark.django_db
def test_user_password_is_hashed():
    user = User.objects.create_user(
        email="test@example.com",
        password="secret123"
    )

    assert user.password != "secret123"
    assert user.check_password("secret123")

@pytest.mark.django_db
def test_user_requeires_email():
    with pytest.raises(ValueError, match="The email must be set"):
        User.objects.create_user(
            email="",
            password="secret123"
        )