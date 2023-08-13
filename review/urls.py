from django.urls import path
from review.views import review_upload







urlpatterns=[
    path("reviews/upload/",review_upload,name="review_upload_view"),
    # path("inventory/",include("inventory.urls")),
]