from django.urls import path
from cart.views import cart_upload







urlpatterns=[
    path("carts/upload/",cart_upload,name="cart_upload_view"),
    # path("inventory/",include("inventory.urls")),
]