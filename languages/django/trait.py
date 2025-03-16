class Trait(AbstractElementModel):

    # Qualitative
    social_effects = models.TextField(blank=True, null=True)
    physical_effects = models.TextField(blank=True, null=True)
    skill_effects = models.TextField(blank=True, null=True)
    personality_effects = models.TextField(blank=True, null=True)
    artistic_effects = models.TextField(blank=True, null=True)
    behaviour_effects = models.TextField(blank=True, null=True)

    # Quantitative
    charisma = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    coercion = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    capability = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    compassion = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    creativity = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    courage = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])

    # World
    anti_trait = models.ForeignKey("Trait", on_delete=models.SET_NULL, blank=True, null=True, related_name="trait_anti_trait")
    empowered_abilities = models.ManyToManyField("Ability", blank=True, related_name="trait_empowered_abilities")

    def __str__(self):
        return self.name
