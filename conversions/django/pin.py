from django.db import models
import uuid
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .abstract_element_model import AbstractElementModel

class Pin(AbstractElementModel):

    # Details
    map = models.ForeignKey("Map", on_delete=models.SET_NULL, blank=True, null=True, related_name="pin_map")
    x = models.PositiveIntegerField(blank=True, null=True)
    y = models.PositiveIntegerField(blank=True, null=True)
    z = models.PositiveIntegerField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, blank=True, null=True)
    object_id = models.UUIDField(blank=True, null=True)
    element = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name
