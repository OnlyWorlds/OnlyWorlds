from .abstract_element_model import AbstractElementModel
from django.db import models

class Language(AbstractElementModel):

    # Structure
    phonology = models.TextField(blank=True, null=True)
    grammar = models.TextField(blank=True, null=True)
    lexicon = models.TextField(blank=True, null=True)
    writing = models.TextField(blank=True, null=True)
    classification = models.ForeignKey("Construct", on_delete=models.SET_NULL, blank=True, null=True, related_name="language_classification")

    # World
    status = models.TextField(blank=True, null=True)
    spread = models.ManyToManyField("Location", blank=True, related_name="language_spread")
    dialects = models.ManyToManyField("Language", blank=True, related_name="language_dialects")

    def __str__(self):
        return self.name
