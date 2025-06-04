from .abstract_element_model import AbstractElementModel
from django.core.validators import MaxValueValidator
from django.db import models

class Character(AbstractElementModel):

    # Constitution
    physicality = models.TextField(blank=True, null=True)
    psychology = models.TextField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    species = models.ManyToManyField("Species", blank=True, related_name="character_species")
    traits = models.ManyToManyField("Trait", blank=True, related_name="character_traits")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="character_abilities")

    # Origins
    background = models.TextField(blank=True, null=True)
    motivations = models.TextField(blank=True, null=True)
    birth_date = models.PositiveIntegerField(blank=True, null=True)
    birthplace = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="character_birthplace")
    languages = models.ManyToManyField("Language", blank=True, related_name="character_languages")

    # World
    situation = models.TextField(blank=True, null=True)
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="character_location")
    titles = models.ManyToManyField("Title", blank=True, related_name="character_titles")
    objects = models.ManyToManyField("Object", blank=True, related_name="character_objects")
    institutions = models.ManyToManyField("Institution", blank=True, related_name="character_institutions")

    # Personality
    charisma = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    coercion = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    capability = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    compassion = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    creativity = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    courage = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)

    # Social
    family = models.ManyToManyField("Family", blank=True, related_name="character_family")
    friends = models.ManyToManyField("Character", blank=True, related_name="character_friends")
    rivals = models.ManyToManyField("Character", blank=True, related_name="character_rivals")

    # Games
    backstory = models.TextField(blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    power = models.PositiveIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    hit_points = models.PositiveIntegerField(blank=True, null=True)
    skill_stealth = models.PositiveIntegerField(blank=True, null=True)
    tt_str = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    tt_int = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    tt_con = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    tt_dex = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    tt_wis = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    tt_cha = models.PositiveIntegerField(validators=[MaxValueValidator(20)], blank=True, null=True)
    class = models.TextField(blank=True, null=True)
    alignment = models.TextField(blank=True, null=True)
    equipment = models.ManyToManyField("Object", blank=True, related_name="character_equipment")
    backpack = models.ManyToManyField("Object", blank=True, related_name="character_backpack")
    proficiencies = models.ManyToManyField("Construct", blank=True, related_name="character_proficiencies")
    features = models.ManyToManyField("Trait", blank=True, related_name="character_features")
    spells = models.ManyToManyField("Ability", blank=True, related_name="character_spells")
    inspirations = models.ManyToManyField("Construct", blank=True, related_name="character_inspirations")

    def __str__(self):
        return self.name
