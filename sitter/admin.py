from django.contrib import admin
from .models import Sitter, Day

# Register your models here.


class SitterAdmin(admin.ModelAdmin):
    model = Sitter


class DayAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    model = Day


admin.site.register(Day, DayAdmin)
admin.site.register(Sitter, SitterAdmin)
