# serializers provides validation and conversion between API data and models.
from rest_framework import serializers

# Import the model represented by this serializer.
from apps.requests.models import Request

# This serializer defines the Request fields exposed through the API.
class RequestSerializer(serializers.ModelSerializer):

    # Accept an ordered, non-empty list of criteria from multipart input.
    criteria = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False,
    )

    # Meta configures which model and fields ModelSerializer should use.
    class Meta:

        model = Request

        # The user field is intentionally omitted because ownership comes from
        # the authenticated user, not from client input.
        fields = ("id", "input_file", "criteria", "created_at")

        # Django creates these values; API clients cannot provide or change them.
        read_only_fields = ("id", "created_at")