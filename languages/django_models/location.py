from .abstract_element_model import AbstractElementModel
from django.db import models

class Location(AbstractElementModel):

    # Setting
    form = models.TextField(blank=True, null=True)
    function = models.TextField(blank=True, null=True)
    founding_date = models.PositiveIntegerField(blank=True, null=True)
    parent_location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_parent_location")
    populations = models.ManyToManyField("Collective", blank=True, related_name="location_populations")

    # Politics
    political_climate = models.TextField(blank=True, null=True)
    primary_power = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_primary_power")
    governing_title = models.ForeignKey("Title", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_governing_title")
    secondary_powers = models.ManyToManyField("Institution", blank=True, related_name="location_secondary_powers")
    zone = models.ForeignKey("Zone", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_zone")
    rival = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_rival")
    partner = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_partner")

    # World
    customs = models.TextField(blank=True, null=True)
    founders = models.ManyToManyField("Character", blank=True, related_name="location_founders")
    cults = models.ManyToManyField("Construct", blank=True, related_name="location_cults")
    delicacies = models.ManyToManyField("Species", blank=True, related_name="location_delicacies")

    # Production
    extraction_methods = models.ManyToManyField("Construct", blank=True, related_name="location_extraction_methods")
    extraction_goods = models.ManyToManyField("Construct", blank=True, related_name="location_extraction_goods")
    industry_methods = models.ManyToManyField("Construct", blank=True, related_name="location_industry_methods")
    industry_goods = models.ManyToManyField("Construct", blank=True, related_name="location_industry_goods")

    # Commerce
    infrastructure = models.TextField(blank=True, null=True)
    extraction_markets = models.ManyToManyField("Location", blank=True, related_name="location_extraction_markets")
    industry_markets = models.ManyToManyField("Location", blank=True, related_name="location_industry_markets")
    currencies = models.ManyToManyField("Construct", blank=True, related_name="location_currencies")

    # Construction
    architecture = models.TextField(blank=True, null=True)
    buildings = models.ManyToManyField("Object", blank=True, related_name="location_buildings")
    building_methods = models.ManyToManyField("Construct", blank=True, related_name="location_building_methods")

    # Defense
    defensibility = models.TextField(blank=True, null=True)
    elevation = models.PositiveIntegerField(blank=True, null=True)
    fighters = models.ManyToManyField("Construct", blank=True, related_name="location_fighters")
    defensive_objects = models.ManyToManyField("Object", blank=True, related_name="location_defensive_objects")

    def __str__(self):
        return self.name
