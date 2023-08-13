from django.shortcuts import render
from .form import CustomerUploadForm
# Create your views here.
def customer_upload(request):
    form = CustomerUploadForm()
    return render(request,'customer/customer_upload.html',{'form': form})

# Create your views here.
