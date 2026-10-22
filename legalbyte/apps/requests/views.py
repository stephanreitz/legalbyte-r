# generics provides ready-made API views; permissions controls access.
from rest_framework import generics, permissions

# The Request model is used to query the authenticated user's Requests.
from apps.requests.models import Request

# The serializer validates input and converts Request objects into API data.
from apps.requests.serializers import RequestSerializer

# ListCreateAPIView handles GET for listing and POST for creation.
class RequestListCreateView(generics.ListCreateAPIView):

    # Use RequestSerializer for both input validation and response serialization.
    serializer_class = RequestSerializer

    # Require a valid authenticated user for both GET and POST.
    permission_classes = [permissions.IsAuthenticated]

    # ListCreateAPIView calls this method when handling a GET request.
    def get_queryset(self):

        # Return only Requests owned by the authenticated user.
        return Request.objects.filter(user=self.request.user)
    
    # ListCreateAPIView calls this hook after POST data is validated.
    def perform_create(self, serializer):
        
        # Set ownership from the authenticated user instead of trusting input.
        serializer.save(user=self.request.user)