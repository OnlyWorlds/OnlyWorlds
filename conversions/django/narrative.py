class Narrative(AbstractElementModel):

    # Nature
    history = models.TextField(blank=True, null=True)
    consequences = models.TextField(blank=True, null=True)
    start_date = models.PositiveIntegerField(blank=True, null=True)
    end_date = models.PositiveIntegerField(blank=True, null=True)

    # Involves
    events = models.ManyToManyField("Event", blank=True, related_name="narrative_events")
    characters = models.ManyToManyField("Character", blank=True, related_name="narrative_characters")
    objects = models.ManyToManyField("Object", blank=True, related_name="narrative_objects")
    locations = models.ManyToManyField("Location", blank=True, related_name="narrative_locations")
    species = models.ManyToManyField("Species", blank=True, related_name="narrative_species")
    creatures = models.ManyToManyField("Creature", blank=True, related_name="narrative_creatures")
    institutions = models.ManyToManyField("Institution", blank=True, related_name="narrative_institutions")
    traits = models.ManyToManyField("Trait", blank=True, related_name="narrative_traits")
    collectives = models.ManyToManyField("Collective", blank=True, related_name="narrative_collectives")
    territories = models.ManyToManyField("Territory", blank=True, related_name="narrative_territories")
    abilities = models.ManyToManyField("Ability", blank=True, related_name="narrative_abilities")
    phenomena = models.ManyToManyField("Phenomenon", blank=True, related_name="narrative_phenomena")
    languages = models.ManyToManyField("Language", blank=True, related_name="narrative_languages")
    families = models.ManyToManyField("Family", blank=True, related_name="narrative_families")
    relations = models.ManyToManyField("Relation", blank=True, related_name="narrative_relations")
    titles = models.ManyToManyField("Title", blank=True, related_name="narrative_titles")
    constructs = models.ManyToManyField("Construct", blank=True, related_name="narrative_constructs")

    def __str__(self):
        return self.name
