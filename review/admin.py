from django.contrib import admin

# Register your models here.

from .models import Review
class ReviewAdmin(admin.ModelAdmin):
    list_display=("message","sender","products","date")

admin.site.register(Review,ReviewAdmin)






