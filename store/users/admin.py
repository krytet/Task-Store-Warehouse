from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'),
            {'fields': ('first_name', 'last_name', 'email', 'type_user',
                        'url')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff',
                    'type_user')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',
                   'type_user')


admin.site.register(User, CustomUserAdmin)
