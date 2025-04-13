class Pin(AbstractElementModel):

    # Details
    map = models.ForeignKey("Map", on_delete=models.SET_NULL, blank=True, null=True, related_name="pin_map")
    element = models.ForeignKey("Element", on_delete=models.SET_NULL, blank=True, null=True, related_name="pin_element")
    x = models.PositiveIntegerField(blank=True, null=True)
    y = models.PositiveIntegerField(blank=True, null=True)
    z = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
