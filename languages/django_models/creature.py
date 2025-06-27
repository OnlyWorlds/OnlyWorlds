from .abstract_element_model import AbstractElementModel
from django.db import models

class Creature(AbstractElementModel):

    # Biology
    appearance = models.TextField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    species = models.ManyToManyField("Species", blank=True, related_name="creature_species")

    # Behaviour
    habits = models.TextField(blank=True, null=True)
    demeanor = models.TextField(blank=True, null=True)
    traits = models.ManyToManyField("Trait", blank=True, related_name="creature_traits")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="creature_abilities")
    languages = models.ManyToManyField("Language", blank=True, related_name="creature_languages")

    # World
    status = models.TextField(blank=True, null=True)
    birth_date = models.PositiveIntegerField(blank=True, null=True)
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="creature_location")
    zone = models.ForeignKey("Zone", on_delete=models.SET_NULL, blank=True, null=True, related_name="creature_zone")

    # Ttrpg
    challenge_rating = models.PositiveIntegerField(blank=True, null=True)
    hit_points = models.PositiveIntegerField(blank=True, null=True)
    armor_class = models.PositiveIntegerField(blank=True, null=True)
    speed = models.PositiveIntegerField(blank=True, null=True)
    actions = models.ManyToManyField("Ability", blank=True, related_name="creature_actions")

    def __str__(self):
        return self.name
