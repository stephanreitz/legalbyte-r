from django.urls import path
from apps.users.views import UserRegistrationView

urlpatterns = [
    path("", UserRegistrationView.as_view(), name="user-registration"),
]