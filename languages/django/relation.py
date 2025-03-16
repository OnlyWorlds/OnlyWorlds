class Relation(AbstractElementModel):

    # Nature
    history = models.TextField(blank=True, null=True)
    impact = models.TextField(blank=True, null=True)
    start_date = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.PositiveIntegerField(blank=True, null=True)
    debt = models.PositiveIntegerField(blank=True, null=True)
    events = models.ManyToManyField("Event", blank=True, related_name="relation_events")

    # Involves
    primary_character = models.ForeignKey("Character", on_delete=models.SET_NULL, blank=True, null=True, related_name="relation_primary_character")
    primary_creature = models.ForeignKey("Creature", on_delete=models.SET_NULL, blank=True, null=True, related_name="relation_primary_creature")
    primary_institution = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="relation_primary_institution")
    secondary_characters = models.ManyToManyField("Character", blank=True, related_name="relation_secondary_characters")
    secondary_creatures = models.ManyToManyField("Creature", blank=True, related_name="relation_secondary_creatures")
    secondary_institutions = models.ManyToManyField("Institution", blank=True, related_name="relation_secondary_institutions")

    def __str__(self):
        return self.name
