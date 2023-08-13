from django.shortcuts import render

# Create your views here.
# Create your views here.

from .form import ReviewUploadForm
# Create your views here.
def review_upload(request):
    form = ReviewUploadForm()
    return render(request,'review/review_upload.html',{'form': form})