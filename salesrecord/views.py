from django.shortcuts import render
from .form import SalesRecordUploadForm
# Create your views here.
def salesrecord_upload(request):
    form = SalesRecordUploadForm()
    return render(request,'salesrecord/salesrecord_upload.html',{'form': form})


