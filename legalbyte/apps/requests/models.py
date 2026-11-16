# settings provides the configured custom user model through AUTH_USER_MODEL.
from django.conf import settings

# models provides Django's model and database field classes.
from django.db import models

# This model describes the desired structure of the requests_request table.
# The table is created only after migrations are generated and applied.
class Request(models.Model):

    # Store which user owns the request. CASCADE removes the user's requests
    # if that user is deleted.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Store the file under MEDIA_ROOT/uploads/ and save only its path in the
    # database.
    input_file = models.FileField(upload_to="uploads/")

    # Store the ordered exclusion criteria submitted by the frontend.
    # The list callable creates a new empty list for each Request.
    criteria = models.JSONField(default=list)

    # Store the worksheet selected by the frontend.
    # Existing Requests used the legacy TRATADAS sheet.
    sheet_name = models.CharField(
        max_length=31,
        default="TRATADAS"
    )

    # Store the generated spreadsheet under MEDIA_ROOT/outputs/.
    # Existing Requests have an empty path because they have no output.
    output_file = models.FileField(
        upload_to="outputs/",
        blank=True,
        default="",
    )

    # Let Django record the creation timestamp when the row is first inserted.
    created_at = models.DateTimeField(auto_now_add=True)