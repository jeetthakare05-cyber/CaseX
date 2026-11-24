from django.core.management.base import BaseCommand
from store.models import Product


class Command(BaseCommand):
    help = "Update existing product images using Cloudinary URLs"

    def handle(self, *args, **options):

        image_updates = {
            "phone 17 pro max": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521248/Zootopia__jpu0t4.jpg",

            "Woven Macbook Case (M1/M2/M3/M4/M5)": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521248/Woven_MacBook_Case_-_MacBook_Pro_14_M1_M2_M3_M4_M5_lnqfrx.jpg",

            "Iphone 16 Pro": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521248/zoro_jxbi4o.jpg",

            "Iphone 17 pro": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521247/wanna_escape__aktbxq.jpg",

            "Iphone 14": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521247/Simple_Sun_Moon_Phone_Case_For_iPhone_14_Plus_7_8_X_XS_XR_11_12_13_Pro_Max_Sili_tTDnKTq_u8mzpa.jpg",

            "Airpods Case": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521246/download_3_kdxveo.jpg",

            "Iphone 15": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521246/iphone_15_back_cover_sticker___Porsche_iphone_case_m3vmhb.jpg",

            "Iphone 16": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521246/iphone_16_pro_desert__esq6lw.jpg",

            "Airpods": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521245/Airpods_pro_cases_pgopgn.jpg",

            "Airpods Pro": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521245/download_1_skwh8w.jpg",

            "Iphone 16": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521245/download_2_ubbin5.jpg",

            "Airpods pro": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521245/AirPods_Pro_wqqbt8.jpg",

            "Iphone 17 Pro Max": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521245/Coque_magn%C3%A9tique_en_Pevlar_pour_iPhone_17_Air_16_Plus_15_n4mb1o.jpg",

            "Iphone 15": "https://res.cloudinary.com/ljqsb2vj/image/upload/v1795521245/Capinha_Iphone_j9xzuh.jpg",
        }

        updated_count = 0

        for product_name, image_url in image_updates.items():

            try:
                product = Product.objects.filter(name__iexact=product_name).first()

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

            except Product.MultipleObjectsReturned:
                self.stdout.write(
                    self.style.WARNING(
                        f"Duplicate product name skipped: {product_name}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nFinished! {updated_count} product images updated."
            )
        )