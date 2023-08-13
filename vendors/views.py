

from django.shortcuts import render
from .form import VendorsUploadForm
# Create your views here.
def vendors_upload(request):
    form = VendorsUploadForm()
    return render(request,'vendors/vendors_upload.html',{'form': form})









