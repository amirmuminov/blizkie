from django.contrib import admin
from .models import Meal, Toilet, Mobility, MentalState, LevelSelfServ, City, Place, Patient


# Register your models here.

class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ['name']


class ToiletAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ['name']


class MobilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ['name']


class MentalStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ['name']


class LevelSelfServAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ['name']


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ['name']


class PatientAdmin(admin.ModelAdmin):
    model = Patient


admin.site.register(Meal, MealAdmin)
admin.site.register(Toilet, ToiletAdmin)
admin.site.register(Mobility, MobilityAdmin)
admin.site.register(MentalState, MentalStateAdmin)
admin.site.register(LevelSelfServ, LevelSelfServAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Patient, PatientAdmin)