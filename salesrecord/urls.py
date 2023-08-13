
from django.urls import path
from salesrecord.views import salesrecord_upload





urlpatterns=[
    path("salesrecords/upload/",salesrecord_upload,name="salesrecord_upload_view"),
    # path("inventory/",include("inventory.urls")),
]

