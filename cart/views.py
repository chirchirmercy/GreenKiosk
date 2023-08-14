from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from .form import CartUploadForm
# Create your views here.
def cart_upload(request):
    form = CartUploadForm()
    return render(request,'cart/cart_upload.html',{'form': form})


