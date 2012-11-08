from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BuiltinUserAdmin
from django.contrib import admin

from .models import UserMeta

admin.site.unregister(User)


class UserMetaInline(admin.TabularInline):
    model = UserMeta
    extra = 0


class UserAdmin(BuiltinUserAdmin):
    inlines = [
        UserMetaInline,
    ]

admin.site.register(User, UserAdmin)
