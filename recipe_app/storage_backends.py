from storages.backends.s3boto3 import S3Boto3Storage
from PIL import Image
from io import BytesIO
import sys

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile


class CompressImageMixin:
    def _save(self, name, content):
        condensed_content = self.compressImage(content, name)
        return super(CompressImageMixin, self)._save(name, condensed_content)

    def compressImage(self, uploadedImage, name):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) )
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        return InMemoryUploadedFile(outputIoStream, 'FileField', name, 'image/jpeg', sys.getsizeof(outputIoStream), None)


class LocalMediaStorage(CompressImageMixin, FileSystemStorage):
    pass


class MediaStorage(CompressImageMixin, S3Boto3Storage):
    location = 'media'
    file_overwrite = False
