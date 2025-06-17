from .abstract_element_model import AbstractElementModel
from django.db import models

class Event(AbstractElementModel):

    # Nature
    history = models.TextField(blank=True, null=True)
    challenges = models.TextField(blank=True, null=True)
    consequences = models.TextField(blank=True, null=True)
    start_date = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.PositiveIntegerField(blank=True, null=True)
    triggers = models.ManyToManyField("Event", blank=True, related_name="event_triggers")

    # Involves
    characters = models.ManyToManyField("Character", blank=True, related_name="event_characters")
    objects = models.ManyToManyField("Object", blank=True, related_name="event_objects")
    locations = models.ManyToManyField("Location", blank=True, related_name="event_locations")
    species = models.ManyToManyField("Species", blank=True, related_name="event_species")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="event_creatures")
    institutions = models.ManyToManyField("Institution", blank=True, related_name="event_institutions")
    traits = models.ManyToManyField("Trait", blank=True, related_name="event_traits")
    collectives = models.ManyToManyField("Collective", blank=True, related_name="event_collectives")
    territories = models.ManyToManyField("Territory", blank=True, related_name="event_territories")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="event_abilities")
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="event_phenomena")
    languages = models.ManyToManyField("Language", blank=True, related_name="event_languages")
    families = models.ManyToManyField("Family", blank=True, related_name="event_families")
    relations = models.ManyToManyField("Relation", blank=True, related_name="event_relations")
    titles = models.ManyToManyField("Title", blank=True, related_name="event_titles")
    constructs = models.ManyToManyField("Construct", blank=True, related_name="event_constructs")

    def __str__(self):
        return self.name
