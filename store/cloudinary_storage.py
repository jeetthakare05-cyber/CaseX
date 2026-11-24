import os
import cloudinary
import cloudinary.uploader
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible


@deconstructible
class CloudinaryStorage(Storage):

    def _save(self, name, content):
        result = cloudinary.uploader.upload(
            content,
            folder="casex/products",
            resource_type="image"
        )
        return result["public_id"]

    def _open(self, name, mode="rb"):
        raise NotImplementedError("Cloudinary files cannot be opened locally.")

    def exists(self, name):
        return False

    def url(self, name):
        return cloudinary.CloudinaryImage(name).build_url(secure=True)