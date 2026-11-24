from django.core.management.base import BaseCommand
from store.models import Product


class Command(BaseCommand):
    help = "Update existing product images using Cloudinary URLs"

    def handle(self, *args, **options):

        image_updates = {
            "Iphone 17 pro max": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521248/Zootopia__jpu0t4.jpg",
        }

        updated_count = 0

        for product_name, image_url in image_updates.items():

            try:
                product = Product.objects.get(name=product_name)

                product.image = image_url
                product.save(update_fields=["image"])

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Image updated successfully: {product_name}"
                    )
                )

                updated_count += 1

            except Product.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(
                        f"Product not found: {product_name}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nFinished! {updated_count} product images updated."
            )
        )