from .abstract_element_model import AbstractElementModel
from django.db import models
from ow.elements.models.object import Object as ObjectModel

class Construct(AbstractElementModel):

    # Nature
    rationale = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    reach = models.TextField(blank=True, null=True)
    start_date = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.PositiveIntegerField(blank=True, null=True)
    founder = models.ForeignKey("Character", on_delete=models.SET_NULL, blank=True, null=True, related_name="construct_founder")
    custodian = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="construct_custodian")

    # Involves
    characters = models.ManyToManyField("Character", blank=True, related_name="construct_characters")
    objects = models.ManyToManyField(ObjectModel, blank=True, related_name="construct_objects")  # type: ignore
    locations = models.ManyToManyField("Location", blank=True, related_name="construct_locations")
    species = models.ManyToManyField("Species", blank=True, related_name="construct_species")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="construct_creatures")
    institutions = models.ManyToManyField("Institution", blank=True, related_name="construct_institutions")
    traits = models.ManyToManyField("Trait", blank=True, related_name="construct_traits")
    collectives = models.ManyToManyField("Collective", blank=True, related_name="construct_collectives")
    zones = models.ManyToManyField("Zone", blank=True, related_name="construct_zones")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="construct_abilities")
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="construct_phenomena")
    languages = models.ManyToManyField("Language", blank=True, related_name="construct_languages")
    families = models.ManyToManyField("Family", blank=True, related_name="construct_families")
    relations = models.ManyToManyField("Relation", blank=True, related_name="construct_relations")
    titles = models.ManyToManyField("Title", blank=True, related_name="construct_titles")
    constructs = models.ManyToManyField("Construct", blank=True, related_name="construct_constructs")
    events = models.ManyToManyField("Event", blank=True, related_name="construct_events")
    narratives = models.ManyToManyField("Narrative", blank=True, related_name="construct_narratives")

    def __str__(self):
        return self.name
