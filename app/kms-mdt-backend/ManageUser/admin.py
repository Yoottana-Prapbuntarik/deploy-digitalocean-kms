from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'mobile', 'first_name', 'last_name', 'is_staff',)
    list_filter = ('email', 'mobile', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
admin.site.register(get_user_model(), CustomUserAdmin)
