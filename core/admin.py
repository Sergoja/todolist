from core.models import User
from django.contrib import admin
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):
    fields = (
        'username', 'first_name', 'last_name',
        'email', 'is_staff', 'is_active',
        'date_joined', 'last_login'
    )
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('date_joined', 'last_login')
    search_fields = ['username', 'first_name', 'last_name']


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
