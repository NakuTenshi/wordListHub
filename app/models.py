import os
from django.db import models
from wordListHub.settings import MEDIA_ROOT
from django.core.validators import FileExtensionValidator



def setFilePath(instance, filename):
    return os.path.join(instance.path , filename)

class upload_wordlist(models.Model):
    path = models.CharField(max_length=50, blank=True)
    file = models.FileField(upload_to=setFilePath, validators=[ FileExtensionValidator(allowed_extensions=["txt" ,"list"]) ])
    uploaded_at = models.DateTimeField(auto_now_add=True)