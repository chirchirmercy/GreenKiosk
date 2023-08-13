

# Create your views here.
from django.shortcuts import render
from .form import Register_accountUploadForm
# Create your views here.
def registration_upload(request):
    form = Register_accountUploadForm()
    return render(request,'registration/registration_upload.html',{'form': form})


