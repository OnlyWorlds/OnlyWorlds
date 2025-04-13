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
    tt_str = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(20)])
    tt_int = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(20)])
    tt_con = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(20)])
    tt_dex = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(20)])
    tt_wis = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(20)])
    tt_cha = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(20)])
    actions = models.ManyToManyField("Ability", blank=True, related_name="creature_actions")
    reactions = models.ManyToManyField("Construct", blank=True, related_name="creature_reactions")
    alignment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
