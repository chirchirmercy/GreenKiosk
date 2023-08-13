from django import forms
from.models import Register_account

class Register_accountUploadForm(forms.ModelForm):
    class Meta:
        model= Register_account
        fields= "__all__"