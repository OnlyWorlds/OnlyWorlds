class World(AbstractBaseModel):
    objects = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    api_key = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    version = models.CharField(max_length=255)
    image_url = models.TextField()
    time_format_equivalents = JSONField(default=list)
    time_format_names = JSONField(default=list)
    time_basic_unit = models.CharField(max_length=255)
    time_range_min = models.PositiveIntegerField()
    time_range_max = models.PositiveIntegerField()
    time_current = models.PositiveIntegerField()

    def __str__(self):
        return self.name
