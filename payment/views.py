

# Create your views here.
from django.shortcuts import render
from .form import PaymentUploadForm
# Create your views here.
def payment_upload(request):
    form = PaymentUploadForm()
    return render(request,'payment/payment_upload.html',{'form': form})



