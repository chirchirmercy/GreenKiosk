from django import forms
from.models import SalesRecord

class SalesRecordUploadForm(forms.ModelForm):
    class Meta:
        model= SalesRecord
        fields= "__all__"