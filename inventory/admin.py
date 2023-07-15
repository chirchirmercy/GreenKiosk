from django.contrib import admin
from.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=("names","stock","price","date_updated","date_created","description","image")

admin.site.register(Product,ProductAdmin)



