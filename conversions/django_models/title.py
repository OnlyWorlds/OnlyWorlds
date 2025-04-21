from .abstract_element_model import AbstractElementModel
from django.db import models

class Title(AbstractElementModel):

    # Nature
    privileges = models.TextField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    create_date = models.PositiveIntegerField(blank=True, null=True)
    assign_date = models.PositiveIntegerField(blank=True, null=True)
    revoke_date = models.PositiveIntegerField(blank=True, null=True)
    hierarchy = models.PositiveIntegerField(blank=True, null=True)

    # Issue
    rights = models.TextField(blank=True, null=True)
    author = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_author")

    # World
    character = models.ForeignKey("Character", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_character")
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_location")
    object = models.ForeignKey("Object", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_object")
    institution = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_institution")
    creature = models.ForeignKey("Creature", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_creature")
    territory = models.ForeignKey("Territory", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_territory")
    collective = models.ForeignKey("Collective", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_collective")
    construct = models.ForeignKey("Construct", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_construct")

    def __str__(self):
        return self.name
