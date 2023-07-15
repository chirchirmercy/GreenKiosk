from django.contrib import admin

# Register your models here.
from .models import Register_account
class Register_accountAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","password","email","phone_number","adress")

admin.site.register(Register_account,Register_accountAdmin)