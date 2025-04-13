class Map(AbstractElementModel):

    # Details
    background_color = models.TextField(blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    map = models.ForeignKey("Map", on_delete=models.SET_NULL, blank=True, null=True, related_name="map_map")

    def __str__(self):
        return self.name
