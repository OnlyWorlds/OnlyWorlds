from .abstract_element_model import AbstractElementModel
from django.db import models

class Family(AbstractElementModel):

    # Community
    spirit = models.TextField(blank=True, null=True)
    alliances = models.ManyToManyField("Family", blank=True, related_name="family_alliances")
    rivalries = models.ManyToManyField("Family", blank=True, related_name="family_rivalries")

    # Lineage
    history = models.TextField(blank=True, null=True)
    ancestors = models.ManyToManyField("Character", blank=True, related_name="family_ancestors")
    traits = models.ManyToManyField("Trait", blank=True, related_name="family_traits")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="family_abilities")
    languages = models.ManyToManyField("Language", blank=True, related_name="family_languages")

    # World
    status = models.TextField(blank=True, null=True)
    competition = models.ManyToManyField("Institution", blank=True, related_name="family_competition")
    administrates = models.ManyToManyField("Institution", blank=True, related_name="family_administrates")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="family_creatures")

    # Legacy
    traditions = models.TextField(blank=True, null=True)
    estate = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="family_estate")
    heirlooms = models.ManyToManyField("Object", blank=True, related_name="family_heirlooms")

    def __str__(self):
        return self.name
