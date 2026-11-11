# path declares URL routes inside this app.
from django.urls import path

# Import the view responsible for listing and creating Requests.
from apps.requests.views import (RequestListCreateView, RequestOutputDownloadView)


# These routes are appended to the prefix declared in config/urls.py.
urlpatterns = [
    
    # GET lists Requests and POST creates one at /api/requests/.
    path("", RequestListCreateView.as_view(), name="request-list-create"),

    # Download the processed output owned by the authenticated user.
    path(
        "<int:request_id>/download/",
        RequestOutputDownloadView.as_view(),
        name="request-output-download",
    ),
    
]