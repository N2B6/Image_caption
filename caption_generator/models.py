
from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    caption = models.TextField(blank=True, null=True)
