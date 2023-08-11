from django.urls import path
from.views import product_upload_view,products_list

urlpatterns=[
    path("products/upload/",product_upload_view,name="product_uploadview"),
    path("products/list/",products_list,name="products_list"),
]




