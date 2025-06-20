from .abstract_element_model import AbstractElementModel
from django.db import models

class Marker(AbstractElementModel):

    # Details
    x = models.PositiveIntegerField(blank=True, null=True)
    y = models.PositiveIntegerField(blank=True, null=True)
    z = models.PositiveIntegerField(blank=True, null=True)
    map = models.ForeignKey("Map", on_delete=models.SET_NULL, blank=True, null=True, related_name="marker_map")
    zone = models.ForeignKey("Zone", on_delete=models.SET_NULL, blank=True, null=True, related_name="marker_zone")

    def __str__(self):
        return self.name
