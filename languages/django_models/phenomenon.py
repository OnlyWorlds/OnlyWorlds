from .abstract_element_model import AbstractElementModel
from django.db import models

class Phenomenon(AbstractElementModel):

    # Mechanics
    expression = models.TextField(blank=True, null=True)
    effects = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    catalysts = models.ManyToManyField("Object", blank=True, related_name="phenomenon_catalysts")
    empowerments = models.ManyToManyField("Ability", blank=True, related_name="phenomenon_empowerments")

    # World
    mythology = models.TextField(blank=True, null=True)
    system = models.ForeignKey("Phenomenon", on_delete=models.SET_NULL, blank=True, null=True, related_name="phenomenon_system")
    triggers = models.ManyToManyField("Construct", blank=True, related_name="phenomenon_triggers")
    wielders = models.ManyToManyField("Character", blank=True, related_name="phenomenon_wielders")
    environments = models.ManyToManyField("Location", blank=True, related_name="phenomenon_environments")

    def __str__(self):
        return self.name
