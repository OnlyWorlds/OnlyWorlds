from .abstract_element_model import AbstractElementModel
from django.core.validators import MaxValueValidator
from django.db import models

class Character(AbstractElementModel):

    # Constitution
    physicality = models.TextField(blank=True, null=True)
    mentality = models.TextField(blank=True, null=True)
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
    reputation = models.TextField(blank=True, null=True)
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True, related_name="character_location")
    objects = models.ManyToManyField("Object", blank=True, related_name="character_objects")
    institutions = models.ManyToManyField("Institution", blank=True, related_name="character_institutions")

    # Personality
    charisma = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    coercion = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    competence = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    compassion = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    creativity = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)
    courage = models.PositiveIntegerField(validators=[MaxValueValidator(100)], blank=True, null=True)

    # Social
    family = models.ManyToManyField("Family", blank=True, related_name="character_family")
    friends = models.ManyToManyField("Character", blank=True, related_name="character_friends")
    rivals = models.ManyToManyField("Character", blank=True, related_name="character_rivals")

    # Ttrpg
    level = models.PositiveIntegerField(blank=True, null=True)
    STR = models.PositiveIntegerField(blank=True, null=True)
    DEX = models.PositiveIntegerField(blank=True, null=True)
    CON = models.PositiveIntegerField(blank=True, null=True)
    INT = models.PositiveIntegerField(blank=True, null=True)
    WIS = models.PositiveIntegerField(blank=True, null=True)
    CHA = models.PositiveIntegerField(blank=True, null=True)
    hit_points = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
