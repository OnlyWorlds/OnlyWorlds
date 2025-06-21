from .abstract_element_model import AbstractElementModel
from django.db import models

class Zone(AbstractElementModel):

    # Scope
    role = models.TextField(blank=True, null=True)
    start_date = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.PositiveIntegerField(blank=True, null=True)
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="zone_phenomena")
    linked_zones = models.ManyToManyField("Zone", blank=True, related_name="zone_linked_zones")

    # World
    context = models.TextField(blank=True, null=True)
    populations = models.ManyToManyField("Collective", blank=True, related_name="zone_populations")
    titles = models.ManyToManyField("Title", blank=True, related_name="zone_titles")
    principles = models.ManyToManyField("Construct", blank=True, related_name="zone_principles")

    def __str__(self):
        return self.name
