from django.contrib import admin

# Register your models here.

from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display=("order_number","order_total","customer","date","products","delivery_date","payment_options")
admin.site.register(Order,OrderAdmin)    









