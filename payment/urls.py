from django.urls import path
from payment.views import payment_upload







urlpatterns=[
    path("payments/upload/",payment_upload,name="payment_upload_view"),
    # path("inventory/",include("inventory.urls")),
]



