from .abstract_element_model import AbstractElementModel
from django.db import models

class Institution(AbstractElementModel):

    # Foundation
    premise = models.TextField(blank=True, null=True)
    found_date = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.PositiveIntegerField(blank=True, null=True)
    parent_institution = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="institution_parent_institution")

    # Claim
    territories = models.ManyToManyField("Territory", blank=True, related_name="institution_territories")
    objects = models.ManyToManyField("Object", blank=True, related_name="institution_objects")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="institution_creatures")
    legal = models.ManyToManyField("Law", blank=True, related_name="institution_legal")

    # World
    situation = models.TextField(blank=True, null=True)
    cooperates = models.ManyToManyField("Institution", blank=True, related_name="institution_cooperates")
    competition = models.ManyToManyField("Institution", blank=True, related_name="institution_competition")
    constructs = models.ManyToManyField("Construct", blank=True, related_name="institution_constructs")
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="institution_phenomena")

    def __str__(self):
        return self.name
