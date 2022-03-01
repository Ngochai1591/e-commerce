from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username', 'first_name', 'last_name')
    readonly_fields  = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    #Required declare
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        ( None, 
            {
                'fields':('email','password')
            }),
        ('Personal Info',
            {
                'fields':('first_name', 'last_name')
            }),
        ('Permission', 
            {
                'fields':('is_active','is_staff','is_superadmin','is_admin')
            }),
        ('Important dates', {
            'fields':('last_login','date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username', 'password1', 'password2', 'first_name', 'last_name'),
        }),
    )

admin.site.register(Account, AccountAdmin)