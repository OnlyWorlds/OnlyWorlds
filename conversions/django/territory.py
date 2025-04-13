from django.db import models
from .abstract_element_model import AbstractElementModel

class Territory(AbstractElementModel):

    # Situation
    terrain = models.TextField(blank=True, null=True)
    size = models.PositiveIntegerField(blank=True, null=True)
    parent_territory = models.ForeignKey("Territory", on_delete=models.SET_NULL, blank=True, null=True, related_name="territory_parent_territory")

    # Yield
    maintenance = models.TextField(blank=True, null=True)
    primary_output = models.PositiveIntegerField(blank=True, null=True)
    secondary_output = models.PositiveIntegerField(blank=True, null=True)
    primary_resource = models.ForeignKey("Construct", on_delete=models.SET_NULL, blank=True, null=True, related_name="territory_primary_resource")
    secondary_resources = models.ManyToManyField("Construct", blank=True, related_name="territory_secondary_resources")

    # World
    history = models.TextField(blank=True, null=True)
    occupants = models.ManyToManyField("Species", blank=True, related_name="territory_occupants")
    occurrences = models.ManyToManyField("Phenomenon", blank=True, related_name="territory_occurrences")

    def __str__(self):
        return self.name
