import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings
from store.models import Product


class Command(BaseCommand):
    help = "Import products from products_only.json"

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, "products_only.json")

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR("products_only.json not found"))
            return

        with open(file_path, encoding="utf-8") as file:
            products = json.load(file)

        created_count = 0

        for item in products:
            fields = item.get("fields", {})
            product_name = fields.get("name")

            if not product_name:
                continue

            if Product.objects.filter(name=product_name).exists():
                continue

            Product.objects.create(**fields)
            created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Import finished! {created_count} new products imported."
            )
        )