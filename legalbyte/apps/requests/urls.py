# path declares URL routes inside this app.
from django.urls import path
# Import the view that handles Request creation.
from apps.requests.views import RequestCreateView

# These routes are appended to the prefix declared in config/urls.py.
urlpatterns = [
    # The empty path completes /api/requests/ and maps POST to CreateAPIView.
    # as_view() converts the class-based view into a callable Django can route.
    path("", RequestCreateView.as_view(), name="request-create"),
]