from .abstract_element_model import AbstractElementModel
from django.db import models

class Object(AbstractElementModel):

    # Form
    aesthetics = models.TextField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    parent_object = models.ForeignKey("Object", on_delete=models.SET_NULL, blank=True, null=True, related_name="object_parent_object")
    materials = models.ManyToManyField("Construct", blank=True, related_name="object_materials")
    technology = models.ManyToManyField("Construct", blank=True, related_name="object_technology")

    # Function
    utility = models.TextField(blank=True, null=True)
    effects = models.ManyToManyField("Phenomenon", blank=True, related_name="object_effects")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="object_abilities")
    consumes = models.ManyToManyField("Construct", blank=True, related_name="object_consumes")

    # World
    origins = models.TextField(blank=True, null=True)
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="object_location")
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, blank=True, null=True, related_name="object_language")
    affinities = models.ManyToManyField("Trait", blank=True, related_name="object_affinities")

    def __str__(self):
        return self.name
