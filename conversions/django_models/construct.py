from .abstract_element_model import AbstractElementModel
from django.db import models

class Construct(AbstractElementModel):

    # Nature
    history = models.TextField(blank=True, null=True)
    understanding = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    start_date = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.PositiveIntegerField(blank=True, null=True)
    founder = models.ForeignKey("Character", on_delete=models.SET_NULL, blank=True, null=True, related_name="construct_founder")
    organiser = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="construct_organiser")

    # Involves
    characters = models.ManyToManyField("Character", blank=True, related_name="construct_characters")
    objects = models.ManyToManyField("Object", blank=True, related_name="construct_objects")
    locations = models.ManyToManyField("Location", blank=True, related_name="construct_locations")
    species = models.ManyToManyField("Species", blank=True, related_name="construct_species")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="construct_creatures")
    institutions = models.ManyToManyField("Institution", blank=True, related_name="construct_institutions")
    traits = models.ManyToManyField("Trait", blank=True, related_name="construct_traits")
    collectives = models.ManyToManyField("Collective", blank=True, related_name="construct_collectives")
    territories = models.ManyToManyField("Territory", blank=True, related_name="construct_territories")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="construct_abilities")
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="construct_phenomena")
    languages = models.ManyToManyField("Language", blank=True, related_name="construct_languages")
    families = models.ManyToManyField("Family", blank=True, related_name="construct_families")
    relations = models.ManyToManyField("Relation", blank=True, related_name="construct_relations")
    titles = models.ManyToManyField("Title", blank=True, related_name="construct_titles")
    constructs = models.ManyToManyField("Construct", blank=True, related_name="construct_constructs")

    def __str__(self):
        return self.name
