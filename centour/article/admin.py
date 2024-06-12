from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Article


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)
