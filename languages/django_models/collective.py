from .abstract_element_model import AbstractElementModel
from django.db import models

class Collective(AbstractElementModel):

    # Formation
    composition = models.TextField(blank=True, null=True)
    count = models.PositiveIntegerField(blank=True, null=True)
    formation_date = models.PositiveIntegerField(blank=True, null=True)
    operator = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="collective_operator")
    equipment = models.ManyToManyField("Construct", blank=True, related_name="collective_equipment")

    # Agency
    activity = models.TextField(blank=True, null=True)
    temperance = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField("Ability", blank=True, related_name="collective_skills")
    rituals = models.ManyToManyField("Construct", blank=True, related_name="collective_rituals")

    # World
    species = models.ManyToManyField("Species", blank=True, related_name="collective_species")
    characters = models.ManyToManyField("Character", blank=True, related_name="collective_characters")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="collective_creatures")
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="collective_phenomena")

    def __str__(self):
        return self.name
