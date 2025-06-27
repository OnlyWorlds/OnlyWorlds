from .abstract_element_model import AbstractElementModel
from django.db import models

class Family(AbstractElementModel):

    # Identity
    spirit = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    traditions = models.ManyToManyField("Construct", blank=True, related_name="family_traditions")
    traits = models.ManyToManyField("Trait", blank=True, related_name="family_traits")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="family_abilities")
    languages = models.ManyToManyField("Language", blank=True, related_name="family_languages")
    ancestors = models.ManyToManyField("Character", blank=True, related_name="family_ancestors")

    # World
    reputation = models.TextField(blank=True, null=True)
    estates = models.ManyToManyField("Location", blank=True, related_name="family_estates")
    governs = models.ManyToManyField("Institution", blank=True, related_name="family_governs")
    heirlooms = models.ManyToManyField("Object", blank=True, related_name="family_heirlooms")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="family_creatures")

    def __str__(self):
        return self.name
