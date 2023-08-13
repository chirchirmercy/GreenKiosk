from django import forms
from.models import Vendors

class VendorsUploadForm(forms.ModelForm):
    class Meta:
        model= Vendors
        fields= "__all__"