from .abstract_element_model import AbstractElementModel
from django.db import models

class Title(AbstractElementModel):

    # Mandate
    authority = models.TextField(blank=True, null=True)
    eligibility = models.TextField(blank=True, null=True)
    grant_date = models.PositiveIntegerField(blank=True, null=True)
    revoke_date = models.PositiveIntegerField(blank=True, null=True)
    issuer = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_issuer")
    body = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_body")
    superior_title = models.ForeignKey("Title", on_delete=models.SET_NULL, blank=True, null=True, related_name="title_superior_title")
    holders = models.ManyToManyField("Character", blank=True, related_name="title_holders")
    symbols = models.ManyToManyField("Object", blank=True, related_name="title_symbols")

    # World
    status = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    characters = models.ManyToManyField("Character", blank=True, related_name="title_characters")
    institutions = models.ManyToManyField("Institution", blank=True, related_name="title_institutions")
    families = models.ManyToManyField("Family", blank=True, related_name="title_families")
    zones = models.ManyToManyField("Zone", blank=True, related_name="title_zones")
    locations = models.ManyToManyField("Location", blank=True, related_name="title_locations")
    objects = models.ManyToManyField("Object", blank=True, related_name="title_objects")
    constructs = models.ManyToManyField("Construct", blank=True, related_name="title_constructs")
    laws = models.ManyToManyField("Law", blank=True, related_name="title_laws")
    collectives = models.ManyToManyField("Collective", blank=True, related_name="title_collectives")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="title_creatures")
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="title_phenomena")
    species = models.ManyToManyField("Species", blank=True, related_name="title_species")
    languages = models.ManyToManyField("Language", blank=True, related_name="title_languages")

    def __str__(self):
        return self.name
