from .abstract_element_model import AbstractElementModel
from django.core.validators import MaxValueValidator
from django.db import models

class Ability(AbstractElementModel):

    # Mechanics
    usage = models.TextField(blank=True, null=True)
    range = models.PositiveIntegerField(blank=True, null=True)
    strength = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    effects = models.ManyToManyField("Phenomenon", blank=True, related_name="ability_effects")
    utility = models.ManyToManyField("Construct", blank=True, related_name="ability_utility")

    # Dynamics
    difficulty = models.TextField(blank=True, null=True)
    talent = models.ManyToManyField("Trait", blank=True, related_name="ability_talent")
    enablers = models.ManyToManyField("Object", blank=True, related_name="ability_enablers")
    requirements = models.ManyToManyField("Construct", blank=True, related_name="ability_requirements")

    # World
    prevalence = models.TextField(blank=True, null=True)
    system = models.ForeignKey("Phenomenon", on_delete=models.SET_NULL, blank=True, null=True, related_name="ability_system")
    construct = models.ForeignKey("Construct", on_delete=models.SET_NULL, blank=True, null=True, related_name="ability_construct")

    def __str__(self):
        return self.name
