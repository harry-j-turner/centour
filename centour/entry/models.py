import uuid

from django.contrib.gis.db import models
from guardian.models import UserObjectPermissionBase, GroupObjectPermissionBase


class Entry(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    is_public = models.BooleanField(default=False)

    title = models.CharField(max_length=255)
    content = models.TextField()
    location = models.PointField(srid=4326, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "entries"


class EntryUserObjectPermission(UserObjectPermissionBase):
    content_object = models.ForeignKey(Entry, on_delete=models.CASCADE)


class EntryGroupObjectPermission(GroupObjectPermissionBase):
    content_object = models.ForeignKey(Entry, on_delete=models.CASCADE)
