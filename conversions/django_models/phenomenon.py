from .abstract_element_model import AbstractElementModel
from django.db import models

class Phenomenon(AbstractElementModel):

    # Manifest
    presence = models.TextField(blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank=True, null=True)
    intensity = models.TextField(blank=True, null=True)
    empowerments = models.ManyToManyField("Trait", blank=True, related_name="phenomenon_empowerments")
    environments = models.ManyToManyField("Location", blank=True, related_name="phenomenon_environments")
    carriers = models.ManyToManyField("Species", blank=True, related_name="phenomenon_carriers")

    # Actuate
    effect = models.TextField(blank=True, null=True)
    catalysts = models.ForeignKey("Object", on_delete=models.SET_NULL, blank=True, null=True, related_name="phenomenon_catalysts")
    wielders = models.ManyToManyField("Character", blank=True, related_name="phenomenon_wielders")
    handlers = models.ManyToManyField("Institution", blank=True, related_name="phenomenon_handlers")
    enablers = models.ManyToManyField("Character", blank=True, related_name="phenomenon_enablers")
    triggers = models.ManyToManyField("Construct", blank=True, related_name="phenomenon_triggers")
    affinity = models.ManyToManyField("Phenomenon", blank=True, related_name="phenomenon_affinity")

    def __str__(self):
        return self.name
