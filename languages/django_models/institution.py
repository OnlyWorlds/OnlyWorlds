from .abstract_element_model import AbstractElementModel
from django.db import models
from ow.elements.models.object import Object as ObjectModel

class Institution(AbstractElementModel):

    # Foundation
    doctrine = models.TextField(blank=True, null=True)
    founding_date = models.PositiveIntegerField(blank=True, null=True)
    parent_institution = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="institution_parent_institution")

    # Claims
    zones = models.ManyToManyField("Zone", blank=True, related_name="institution_zones")
    objects = models.ManyToManyField(ObjectModel, blank=True, related_name="institution_objects")  # type: ignore
    creatures = models.ManyToManyField("Creature", blank=True, related_name="institution_creatures")

    # World
    status = models.TextField(blank=True, null=True)
    allies = models.ManyToManyField("Institution", blank=True, related_name="institution_allies")
    adversaries = models.ManyToManyField("Institution", blank=True, related_name="institution_adversaries")
    constructs = models.ManyToManyField("Construct", blank=True, related_name="institution_constructs")

    def __str__(self):
        return self.name
