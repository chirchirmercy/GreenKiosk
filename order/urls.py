from django.urls import path
from order.views import order_upload



urlpatterns=[
    path("orders/upload/",order_upload,name="order_upload_view"),
    # path("inventory/",include("inventory.urls")),
]
