from django.urls import path
from vendors.views import vendors_upload







urlpatterns=[
    path("vendors/upload/",vendors_upload,name="vendors_upload_view"),
    # path("inventory/",include("inventory.urls")),
]
