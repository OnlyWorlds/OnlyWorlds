from django.db import models
from django.core.validators import MaxValueValidator
from .abstract_element_model import AbstractElementModel

class Location(AbstractElementModel):

    # Locality
    scene = models.TextField(blank=True, null=True)
    activity = models.TextField(blank=True, null=True)
    founding_date = models.PositiveIntegerField(blank=True, null=True)
    population_size = models.PositiveIntegerField(blank=True, null=True)
    parent_location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_parent_location")
    populations = models.ManyToManyField("Collective", blank=True, related_name="location_populations")

    # Culture
    traditions = models.TextField(blank=True, null=True)
    celebrations = models.TextField(blank=True, null=True)
    primary_cult = models.ForeignKey("Construct", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_primary_cult")
    secondary_cults = models.ManyToManyField("Construct", blank=True, related_name="location_secondary_cults")
    delicacies = models.ManyToManyField("Species", blank=True, related_name="location_delicacies")

    # World
    coordinates = models.TextField(blank=True, null=True)
    founders = models.ManyToManyField("Character", blank=True, related_name="location_founders")

    # Construction
    logistics = models.TextField(blank=True, null=True)
    architecture = models.TextField(blank=True, null=True)
    construction_rate = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    buildings = models.ManyToManyField("Location", blank=True, related_name="location_buildings")
    building_expertise = models.ManyToManyField("Construct", blank=True, related_name="location_building_expertise")

    # Production
    extraction = models.TextField(blank=True, null=True)
    industry = models.TextField(blank=True, null=True)
    extraction_output = models.PositiveIntegerField(blank=True, null=True)
    industry_output = models.PositiveIntegerField(blank=True, null=True)
    primary_resource = models.ForeignKey("Construct", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_primary_resource")
    primary_industry = models.ForeignKey("Construct", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_primary_industry")
    secondary_resources = models.ManyToManyField("Construct", blank=True, related_name="location_secondary_resources")
    secondary_industries = models.ManyToManyField("Construct", blank=True, related_name="location_secondary_industries")

    # Commerce
    trade = models.TextField(blank=True, null=True)
    infrastructure = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    primary_extraction_market = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_primary_extraction_market")
    primary_industry_market = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_primary_industry_market")
    secondary_extraction_markets = models.ManyToManyField("Location", blank=True, related_name="location_secondary_extraction_markets")
    secondary_industry_markets = models.ManyToManyField("Location", blank=True, related_name="location_secondary_industry_markets")

    # Localpolitics
    government = models.TextField(blank=True, null=True)
    opposition = models.TextField(blank=True, null=True)
    governing_title = models.ForeignKey("Title", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_governing_title")
    primary_faction = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_primary_faction")
    secondary_factions = models.ManyToManyField("Institution", blank=True, related_name="location_secondary_factions")

    # Regionalpolitics
    territorial_policies = models.TextField(blank=True, null=True)
    territory = models.ForeignKey("Territory", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_territory")
    rival = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_rival")
    friend = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_friend")
    soft_influence_on = models.ManyToManyField("Location", blank=True, related_name="location_soft_influence_on")
    hard_influence_on = models.ManyToManyField("Location", blank=True, related_name="location_hard_influence_on")

    # Strategics
    defensibility = models.TextField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    primary_fighter = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="location_primary_fighter")
    secondary_fighters = models.ManyToManyField("Institution", blank=True, related_name="location_secondary_fighters")
    defenses = models.ManyToManyField("Location", blank=True, related_name="location_defenses")
    fortifications = models.ManyToManyField("Object", blank=True, related_name="location_fortifications")

    def __str__(self):
        return self.name
