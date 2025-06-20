from .abstract_element_model import AbstractElementModel
from django.core.validators import MaxValueValidator
from django.db import models

class Ability(AbstractElementModel):

    # Mechanics
    activation = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    potency = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    range = models.PositiveIntegerField(blank=True, null=True)
    effects = models.ManyToManyField("Phenomenon", blank=True, related_name="ability_effects")

    # Enablement
    challenges = models.TextField(blank=True, null=True)
    source = models.ForeignKey("Phenomenon", on_delete=models.SET_NULL, blank=True, null=True, related_name="ability_source")
    talents = models.ManyToManyField("Trait", blank=True, related_name="ability_talents")
    instruments = models.ManyToManyField("Object", blank=True, related_name="ability_instruments")
    requisites = models.ManyToManyField("Construct", blank=True, related_name="ability_requisites")

    # World
    prevalence = models.TextField(blank=True, null=True)
    tradition = models.ForeignKey("Construct", on_delete=models.SET_NULL, blank=True, null=True, related_name="ability_tradition")
    locus = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="ability_locus")

    def __str__(self):
        return self.name
