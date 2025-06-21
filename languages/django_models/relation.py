from .abstract_element_model import AbstractElementModel
from django.core.validators import MaxValueValidator
from django.db import models

class Relation(AbstractElementModel):

    # Nature
    background = models.TextField(blank=True, null=True)
    start_date = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.PositiveIntegerField(blank=True, null=True)
    intensity = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    actor = models.ForeignKey("Character", on_delete=models.SET_NULL, blank=True, null=True, related_name="relation_actor")
    events = models.ManyToManyField("Event", blank=True, related_name="relation_events")

    # Involves
    characters = models.ManyToManyField("Character", blank=True, related_name="relation_characters")
    objects = models.ManyToManyField("Object", blank=True, related_name="relation_objects")
    locations = models.ManyToManyField("Location", blank=True, related_name="relation_locations")
    species = models.ManyToManyField("Species", blank=True, related_name="relation_species")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="relation_creatures")
    institutions = models.ManyToManyField("Institution", blank=True, related_name="relation_institutions")
    traits = models.ManyToManyField("Trait", blank=True, related_name="relation_traits")
    collectives = models.ManyToManyField("Collective", blank=True, related_name="relation_collectives")
    zones = models.ManyToManyField("Zone", blank=True, related_name="relation_zones")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="relation_abilities")
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="relation_phenomena")
    languages = models.ManyToManyField("Language", blank=True, related_name="relation_languages")
    families = models.ManyToManyField("Family", blank=True, related_name="relation_families")
    titles = models.ManyToManyField("Title", blank=True, related_name="relation_titles")
    constructs = models.ManyToManyField("Construct", blank=True, related_name="relation_constructs")
    events = models.ManyToManyField("Event", blank=True, related_name="relation_events")
    narratives = models.ManyToManyField("Narrative", blank=True, related_name="relation_narratives")

    def __str__(self):
        return self.name
