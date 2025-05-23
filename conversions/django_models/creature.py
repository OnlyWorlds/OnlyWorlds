from .abstract_element_model import AbstractElementModel
from django.core.validators import MaxValueValidator
from django.db import models

class Creature(AbstractElementModel):

    # Physiology
    appearance = models.TextField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    species = models.ManyToManyField("Species", blank=True, related_name="creature_species")

    # Lifestyle
    behaviour = models.TextField(blank=True, null=True)
    demeanour = models.TextField(blank=True, null=True)
    traits = models.ManyToManyField("Trait", blank=True, related_name="creature_traits")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="creature_abilities")
    languages = models.ManyToManyField("Language", blank=True, related_name="creature_languages")

    # World
    birth_date = models.PositiveIntegerField(blank=True, null=True)
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="creature_location")
    territory = models.ForeignKey("Territory", on_delete=models.SET_NULL, blank=True, null=True, related_name="creature_territory")

    # Games
    lore = models.TextField(blank=True, null=True)
    senses = models.TextField(blank=True, null=True)
    hit_points = models.PositiveIntegerField(blank=True, null=True)
    armor_class = models.PositiveIntegerField(blank=True, null=True)
    challenge_rating = models.PositiveIntegerField(blank=True, null=True)
    speed = models.PositiveIntegerField(blank=True, null=True)
    tt_str = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    tt_int = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    tt_con = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    tt_dex = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    tt_wis = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    tt_cha = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    actions = models.ManyToManyField("Ability", blank=True, related_name="creature_actions")
    reactions = models.ManyToManyField("Construct", blank=True, related_name="creature_reactions")
    alignment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
