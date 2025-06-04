from .abstract_element_model import AbstractElementModel
from django.db import models

class Marker(AbstractElementModel):

    # Details
    map = models.ForeignKey("Map", on_delete=models.CASCADE, related_name="marker_map")
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    z = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
