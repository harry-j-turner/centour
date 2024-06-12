from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Page


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    pass

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)
