from django.db import models
import uuid

class AbstractElementModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=255)
    description = models.TextField(blank=True, null=True)
    supertype = models.CharField(max_length=255, blank=True, null=True)
    subtype = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    world = models.ForeignKey(
        "worlds.World",
        on_delete=models.CASCADE,
        related_name="%(class)s_related"
    )

    class Meta:
        abstract = True
