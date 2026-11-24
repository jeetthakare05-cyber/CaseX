from django.core.management.base import BaseCommand
import cloudinary.api


class Command(BaseCommand):
    help = "List uploaded CaseX images from Cloudinary"

    def handle(self, *args, **options):

        result = cloudinary.api.resources(
            type="upload",
            prefix="casex/",
            max_results=100
        )

        assets = result.get("resources", [])

        self.stdout.write(f"\nFound {len(assets)} Cloudinary images:\n")

        for asset in assets:
            self.stdout.write(
                f"PUBLIC ID: {asset['public_id']}\n"
                f"URL: {asset['secure_url']}\n"
            )

        self.stdout.write(
            self.style.SUCCESS("\nCloudinary image listing completed.")
        )