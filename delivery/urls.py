from django.urls import path
from delivery.views import delivery_upload





urlpatterns=[
    path("deliveries/upload/",delivery_upload,name="delivery_upload_view"),
    # path("inventory/",include("inventory.urls")),
]