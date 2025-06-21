from .abstract_element_model import AbstractElementModel
from django.core.validators import MaxValueValidator
from django.db import models

class Species(AbstractElementModel):

    # Biology
    appearance = models.TextField(blank=True, null=True)
    life_span = models.PositiveIntegerField(blank=True, null=True)
    typical_weight = models.PositiveIntegerField(blank=True, null=True)
    diet = models.ManyToManyField("Species", blank=True, related_name="species_diet")
    reproduction = models.ManyToManyField("Construct", blank=True, related_name="species_reproduction")

    # Psychology
    instincts = models.TextField(blank=True, null=True)
    sociality = models.TextField(blank=True, null=True)
    temperament = models.TextField(blank=True, null=True)
    communication = models.TextField(blank=True, null=True)
    aggression = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    traits = models.ManyToManyField("Trait", blank=True, related_name="species_traits")

    # World
    role = models.TextField(blank=True, null=True)
    parent_species = models.ForeignKey("Species", on_delete=models.SET_NULL, blank=True, null=True, related_name="species_parent_species")
    locations = models.ManyToManyField("Location", blank=True, related_name="species_locations")
    zones = models.ManyToManyField("Zone", blank=True, related_name="species_zones")
    affinities = models.ManyToManyField("Phenomenon", blank=True, related_name="species_affinities")

    def __str__(self):
        return self.name
