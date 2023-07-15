from django.contrib import admin

# Register your models here.

from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display=("payment_status","payment_method","expiration_date")

admin.site.register(Payment,PaymentAdmin)

