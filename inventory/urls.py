from django.urls import path
from .views import product_detail
from .views import product_upload_view
from .views import products_list

urlpatterns=[
    path("products/upload/",product_upload_view,name="product_upload_view"),
    path("products/list/",products_list,name="products_list_veiw"),
    path("products/<int:id>/",product_detail,name="product_detail_view")
]




