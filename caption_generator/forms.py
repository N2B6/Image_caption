from django import forms
from django.core.exceptions import ValidationError
from .models import UploadedImage

def validate_image_extension(value):
    if not value.name.lower().endswith(('.jpg', '.jpeg', '.heic')):
        raise ValidationError("Only .jpg, .jpeg, and .heic files are allowed.")

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']
    
    image = forms.ImageField(validators=[validate_image_extension])
