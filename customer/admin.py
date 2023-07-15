from django.contrib import admin


# Register your models here.

from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=("names","phone_number","email","adress")
admin.site.register(Customer,CustomerAdmin)
 