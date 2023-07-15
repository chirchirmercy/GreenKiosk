from django.contrib import admin

# Register your models here.
from .models import SalesRecord
class SalesRecordAdmin(admin.ModelAdmin):
    list_display=("sales_date","amount")

admin.site.register(SalesRecord,SalesRecordAdmin)
