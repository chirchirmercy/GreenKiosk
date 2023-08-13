from django.contrib import admin
from.models import  Vendors

# Register your models here.
class VendorsAdmin(admin.ModelAdmin):
    list_display=("first_name","second_name","phone_number")
admin.site.register(Vendors,VendorsAdmin)
