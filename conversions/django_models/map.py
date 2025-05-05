from .abstract_element_model import AbstractElementModel
from django.db import models

class Map(AbstractElementModel):

    # Details
    background_color = models.TextField(blank=True, null=True)
    hierarchy = models.PositiveIntegerField(blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    parent_map = models.ForeignKey("Map", on_delete=models.SET_NULL, blank=True, null=True, related_name="map_parent_map")
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="map_location")

    def __str__(self):
        return self.name
