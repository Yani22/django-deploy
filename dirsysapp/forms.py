from django import forms
from .models import *

class UploadForm(forms.ModelForm):
    author = forms.ModelMultipleChoiceField(queryset=EndUser.objects.all())

    class Meta:
        model = ResearchOutput
        fields = ("title", "author", "file", "image", "date_created")