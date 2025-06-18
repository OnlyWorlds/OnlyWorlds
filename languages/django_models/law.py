from .abstract_element_model import AbstractElementModel
from django.db import models

class Law(AbstractElementModel):

    # Code
    declaration = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    date = models.PositiveIntegerField(blank=True, null=True)
    parent_law = models.ForeignKey("Law", on_delete=models.SET_NULL, blank=True, null=True, related_name="law_parent_law")
    penalties = models.ManyToManyField("Construct", blank=True, related_name="law_penalties")

    # World
    author = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="law_author")
    locations = models.ManyToManyField("Location", blank=True, related_name="law_locations")
    zones = models.ManyToManyField("Zone", blank=True, related_name="law_zones")
    prohibitions = models.ManyToManyField("Construct", blank=True, related_name="law_prohibitions")
    adjudicators = models.ManyToManyField("Title", blank=True, related_name="law_adjudicators")
    enforcers = models.ManyToManyField("Title", blank=True, related_name="law_enforcers")

    def __str__(self):
        return self.name
