from django.db import models
from .abstract_element_model import AbstractElementModel

class Language(AbstractElementModel):

    # Syntax
    writing = models.TextField(blank=True, null=True)
    phonology = models.TextField(blank=True, null=True)
    grammar = models.TextField(blank=True, null=True)
    vocabulary = models.TextField(blank=True, null=True)
    classification = models.ForeignKey("Construct", on_delete=models.SET_NULL, blank=True, null=True, related_name="language_classification")

    # Spread
    prose = models.TextField(blank=True, null=True)
    speakers = models.PositiveIntegerField(blank=True, null=True)
    dialects = models.ManyToManyField("Language", blank=True, related_name="language_dialects")
    range = models.ManyToManyField("Location", blank=True, related_name="language_range")

    def __str__(self):
        return self.name
