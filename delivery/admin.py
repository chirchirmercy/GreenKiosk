from django.contrib import admin
from.models import Delivery

# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    list_display=("delivery_adress","delivery_time","delivery_person","destination")
admin.site.register(Delivery,DeliveryAdmin)




