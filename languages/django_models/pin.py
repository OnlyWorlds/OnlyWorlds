from .abstract_element_model import AbstractElementModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from uuid_extensions import uuid7  # type: ignore

class Pin(AbstractElementModel):

    # Details
    map = models.ForeignKey("Map", on_delete=models.CASCADE, related_name="pin_map")
    element_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    element_id = models.UUIDField(blank=True, null=True)
    element = GenericForeignKey('element_type', 'element_id')
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    z = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
