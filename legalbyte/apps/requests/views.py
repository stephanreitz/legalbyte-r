# generics provides ready-made API views; permissions controls access.
from rest_framework import generics, permissions
# The serializer validates input and creates the Request model instance.
from apps.requests.serializers import RequestSerializer

# CreateAPIView implements the POST flow for creating one Request.
class RequestCreateView(generics.CreateAPIView):
    # Use RequestSerializer to validate the upload and serialize the response.
    serializer_class = RequestSerializer
    # Reject requests without a valid authenticated user, including JWT clients.
    permission_classes = [permissions.IsAuthenticated]

    # CreateAPIView calls this hook after serializer validation succeeds.
    def perform_create(self, serializer):
        # Set ownership from the authenticated JWT user instead of trusting a
        # user ID supplied in the request body.
        serializer.save(user=self.request.user)