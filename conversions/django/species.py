class Species(AbstractElementModel):

    # Biology
    appearance = models.TextField(blank=True, null=True)
    life_span = models.PositiveIntegerField(blank=True, null=True)
    average_weight = models.PositiveIntegerField(blank=True, null=True)
    nourishment = models.ManyToManyField("Species", blank=True, related_name="species_nourishment")

    # Psychology
    instincts = models.TextField(blank=True, null=True)
    aggression = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)])
    agency = models.TextField(blank=True, null=True)
    languages = models.ManyToManyField("Language", blank=True, related_name="species_languages")

    # World
    impact = models.TextField(blank=True, null=True)
    habitat = models.ManyToManyField("Location", blank=True, related_name="species_habitat")
    interaction = models.ManyToManyField("Phenomenon", blank=True, related_name="species_interaction")
    consumables = models.ManyToManyField("Construct", blank=True, related_name="species_consumables")

    def __str__(self):
        return self.name
