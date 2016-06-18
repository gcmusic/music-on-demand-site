from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Artist(models.Model):
    """
    Represents an artist or musical act.
    """
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=32)
    short_desc = models.CharField(max_length=512)
    min_price = models.IntegerField()
    website = models.CharField(max_length=256, blank=True)
    max_dist = models.IntegerField()
    max_dist_inc = models.IntegerField()
    long_desc = models.TextField()
    repertoire = models.TextField(blank=True)
    youtube_id = models.CharField(max_length=64)
    youtube_title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    reg_date = models.DateTimeField("Date registered")

    def __str__(self):
        return self.name
