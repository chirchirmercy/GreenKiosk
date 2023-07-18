from django.contrib import admin

# Register your models here.

from.models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display=("name","quantity","user_id","total_items")
admin.site.register(Cart,CartAdmin)
 

