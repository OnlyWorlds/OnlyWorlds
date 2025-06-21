from .abstract_element_model import AbstractElementModel
from django.db import models

class Zone(AbstractElementModel):

    # Scope
    function = models.TextField(blank=True, null=True)
    start_date = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.PositiveIntegerField(blank=True, null=True)
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="zone_phenomena")

    # World
    history = models.TextField(blank=True, null=True)
    claimed_by = models.ManyToManyField("Institution", blank=True, related_name="zone_claimed_by")
    roamed_by = models.ManyToManyField("Creature", blank=True, related_name="zone_roamed_by")
    titles = models.ManyToManyField("Title", blank=True, related_name="zone_titles")

    def __str__(self):
        return self.name
