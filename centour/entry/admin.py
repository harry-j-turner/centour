from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Entry


@admin.register(Entry)
class EntryAdmin(GuardedModelAdmin):
    list_display = ('uuid', 'title', 'created_at')
