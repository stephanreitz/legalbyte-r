# timedelta represents the three-dau retention interval.
from datetime import timedelta

# BaseCommand is Django's base class for custom management commands.
from django.core.management.base import BaseCommand

# timezone provides timezone-aware dates compatible with Django.
from django.utils import timezone

# Requests stores the file paths and creation timestamp.
from apps.requests.models import Request


class Command(BaseCommand):
    # This text appears in 'python manage.py help'.
    help = "Delete input and output files from Requests older than three days."

    def handle(self, *args, **options):
        # Requests created at or before this data hae expired files.
        retention_limit = timezone.now() - timedelta(days=3)

        expired_requests = Request.objects.filter(
            created_at__lte=retention_limit
        )

        deleted_file_count = 0

        # iterator() avoids loading every expired Request into memory at once.
        for publication_request in expired_requests.iterator():
            file_fields = (
                publication_request.input_file,
                publication_request.output_file,
            )

            for file_field in file_fields:
                file_name = file_field.name

                # Empty fields have no physical file to remove.
                if not file_name:
                    continue

                storage = file_field.storage

                # Delete through Django storage so this also works with S3 later.
                if storage.exists(file_name):
                    storage.delete(file_name)
                    deleted_file_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Deleted {deleted_file_count} expired file(s)."
            )
        )

        


