from django.forms import ModelForm
from .models import upload_wordlist

class uploadwordlistform(ModelForm):
    class Meta:
        model = upload_wordlist
        fields = ["path" , "file"]