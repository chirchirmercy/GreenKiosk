from django.urls import path
from registration.views import registration_upload







urlpatterns=[
    path("registrations/upload/",registration_upload,name="registration_upload_view"),
    # path("inventory/",include("inventory.urls")),
]


