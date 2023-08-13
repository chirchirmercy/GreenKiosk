from django.shortcuts import render

# Create your views here.

from .form import DeliveryUploadForm
# Create your views here.
def delivery_upload(request):
    form = DeliveryUploadForm()
    return render(request,'delivery/delivery_upload.html',{'form': form})



