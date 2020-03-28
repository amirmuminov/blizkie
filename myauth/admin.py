from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.


class CustomerUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'username', 'is_sitter', 'is_patient')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_sitter', 'is_patient')}),
    )


admin.site.register(CustomUser, CustomerUserAdmin)