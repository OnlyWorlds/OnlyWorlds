from django.db import models
from .abstract_element_model import AbstractElementModel

class Object(AbstractElementModel):

    # Form
    aesthetics = models.TextField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    parent_object = models.ForeignKey("Object", on_delete=models.SET_NULL, blank=True, null=True, related_name="object_parent_object")
    technology = models.ManyToManyField("Construct", blank=True, related_name="object_technology")

    # Function
    utility = models.TextField(blank=True, null=True)
    effects = models.ManyToManyField("Phenomenon", blank=True, related_name="object_effects")
    enables = models.ManyToManyField("Ability", blank=True, related_name="object_enables")
    consumes = models.ManyToManyField("Construct", blank=True, related_name="object_consumes")

    # World
    origins = models.TextField(blank=True, null=True)
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="object_location")

    # Games
    craftsmanship = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    durability = models.TextField(blank=True, null=True)
    value = models.PositiveIntegerField(blank=True, null=True)
    damage = models.PositiveIntegerField(blank=True, null=True)
    armor = models.PositiveIntegerField(blank=True, null=True)
    rarity = models.TextField(blank=True, null=True)
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, blank=True, null=True, related_name="object_language")
    requires = models.ManyToManyField("Trait", blank=True, related_name="object_requires")

    def __str__(self):
        return self.name
