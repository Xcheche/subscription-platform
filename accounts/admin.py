from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from import_export.admin import ImportExportModelAdmin

from accounts import models

class CustomUserInline(admin.TabularInline):
    model = models.CustomUser
    can_delete = False
    extra = 1

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email',  'first_name', 'last_name', 'is_staff', 'is_active','date_joined', 'is_writer')
    search_fields = ('email', 'first_name')
    readonly_fields = ('date_joined', )
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ('is_staff', 'is_active', 'is_writer')
    list_editable = ('is_staff', 'is_active', 'is_writer')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email','first_name', 'last_name','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_writer')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser,CustomUserAdmin)
