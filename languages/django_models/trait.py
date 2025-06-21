from .abstract_element_model import AbstractElementModel
from django.core.validators import MaxValueValidator
from django.db import models

class Trait(AbstractElementModel):

    # Qualitative
    social_effects = models.TextField(blank=True, null=True)
    physical_effects = models.TextField(blank=True, null=True)
    functional_effects = models.TextField(blank=True, null=True)
    personality_effects = models.TextField(blank=True, null=True)
    behaviour_effects = models.TextField(blank=True, null=True)

    # Quantitative
    charisma = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    coercion = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    competence = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    compassion = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    creativity = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    courage = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)

    # World
    significance = models.TextField(blank=True, null=True)
    anti_trait = models.ForeignKey("Trait", on_delete=models.SET_NULL, blank=True, null=True, related_name="trait_anti_trait")
    empowered_abilities = models.ManyToManyField("Ability", blank=True, related_name="trait_empowered_abilities")

    def __str__(self):
        return self.name
