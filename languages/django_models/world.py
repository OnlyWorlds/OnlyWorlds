from django.conf import settings
from django.db import models
from django.db.models import JSONField
from uuid_extensions import uuid7  # type: ignore

class World(models.Model):
    objects = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid7, editable=False)
    api_key = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=50, default='0.20.10')
    image_url = models.URLField(blank=True, null=True)
    time_format_equivalents = JSONField(default=list)
    time_format_names = JSONField(default=list)
    time_basic_unit = models.CharField(max_length=50, default='Year')
    time_range_min = models.PositiveIntegerField(default=0)
    time_range_max = models.PositiveIntegerField(default=100)
    time_current = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="worlds")

    def __str__(self):
        return self.name
