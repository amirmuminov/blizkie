from django.contrib import admin
from .models import Advertisement


# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    model = Advertisement
    list_display = ('id', 'author', 'created_on')
    search_fields = ['author']


admin.site.register(Advertisement, AdvertisementAdmin)
