from accounts.models import UserProfile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    extra = 0

class UserProfileAdmin(admin.ModelAdmin):
    verbose_name_plural = 'profile'
    list_display = ('username', 'last_name', 'first_name', 'email', 'is_active', 'is_staff')
    readonly_fields = [
        'last_login',
        'date_joined',
    ]
    inlines = [ UserProfileInline, ]

admin.site.register(User, UserProfileAdmin)
