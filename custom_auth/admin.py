from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone', 'address', 'birth_date', 'is_verified')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address', 'phone',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('address', 'phone',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)