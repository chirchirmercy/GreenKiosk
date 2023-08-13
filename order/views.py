from django.shortcuts import render

# Create your views here.

from .form import OrderUploadForm
# Create your views here.
def order_upload(request):
    form = OrderUploadForm()
    return render(request,'order/order_upload.html',{'form': form})