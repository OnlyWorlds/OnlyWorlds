from .abstract_element_model import AbstractElementModel
from django.db import models

class Narrative(AbstractElementModel):

    # Context
    story = models.TextField(blank=True, null=True)
    consequences = models.TextField(blank=True, null=True)
    start_date = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    parent_narrative = models.ForeignKey("Narrative", on_delete=models.SET_NULL, blank=True, null=True, related_name="narrative_parent_narrative")
    protagonist = models.ForeignKey("Character", on_delete=models.SET_NULL, blank=True, null=True, related_name="narrative_protagonist")
    antagonist = models.ForeignKey("Character", on_delete=models.SET_NULL, blank=True, null=True, related_name="narrative_antagonist")
    narrator = models.ForeignKey("Character", on_delete=models.SET_NULL, blank=True, null=True, related_name="narrative_narrator")
    conservator = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="narrative_conservator")

    # Involves
    events = models.ManyToManyField("Event", blank=True, related_name="narrative_events")
    characters = models.ManyToManyField("Character", blank=True, related_name="narrative_characters")
    objects = models.ManyToManyField("Object", blank=True, related_name="narrative_objects")
    locations = models.ManyToManyField("Location", blank=True, related_name="narrative_locations")
    species = models.ManyToManyField("Species", blank=True, related_name="narrative_species")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="narrative_creatures")
    institutions = models.ManyToManyField("Institution", blank=True, related_name="narrative_institutions")
    traits = models.ManyToManyField("Trait", blank=True, related_name="narrative_traits")
    collectives = models.ManyToManyField("Collective", blank=True, related_name="narrative_collectives")
    zones = models.ManyToManyField("Zone", blank=True, related_name="narrative_zones")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="narrative_abilities")
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="narrative_phenomena")
    languages = models.ManyToManyField("Language", blank=True, related_name="narrative_languages")
    families = models.ManyToManyField("Family", blank=True, related_name="narrative_families")
    relations = models.ManyToManyField("Relation", blank=True, related_name="narrative_relations")
    titles = models.ManyToManyField("Title", blank=True, related_name="narrative_titles")
    constructs = models.ManyToManyField("Construct", blank=True, related_name="narrative_constructs")
    laws = models.ManyToManyField("Law", blank=True, related_name="narrative_laws")

    def __str__(self):
        return self.name
