from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Entry


class EntryAdmin(GuardedModelAdmin):
    list_display = ('uuid', 'title', 'created_at')


admin.site.register(Entry, EntryAdmin)
