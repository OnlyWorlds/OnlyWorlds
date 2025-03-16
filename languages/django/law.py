class Law(AbstractElementModel):

    # Code
    decree = models.TextField(blank=True, null=True)
    date = models.PositiveIntegerField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    author = models.ForeignKey("Institution", on_delete=models.SET_NULL, blank=True, null=True, related_name="law_author")

    # Compulsion
    jurisdictions = models.ManyToManyField("Location", blank=True, related_name="law_jurisdictions")
    prohibitions = models.ManyToManyField("Construct", blank=True, related_name="law_prohibitions")
    penalties = models.ManyToManyField("Construct", blank=True, related_name="law_penalties")
    adjudicators = models.ManyToManyField("Title", blank=True, related_name="law_adjudicators")
    enforcers = models.ManyToManyField("Title", blank=True, related_name="law_enforcers")

    def __str__(self):
        return self.name
