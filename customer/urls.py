from django.urls import path
from customer.views import customer_upload







urlpatterns=[
    path("customers/upload/",customer_upload,name="customer_upload_view"),
    # path("inventory/",include("inventory.urls")),
]