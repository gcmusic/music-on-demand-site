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
    reg_date = models.DateTimeField("Date registered")
    url = models.CharField(max_length=32)
    website = models.CharField(max_length=256, blank=True)
    
    short_desc = models.CharField(max_length=512)
    long_desc = models.TextField()
    repertoire = models.TextField(blank=True)
    
    min_price = models.IntegerField()
    location = models.CharField(max_length=256)
    max_dist = models.IntegerField()
    max_dist_inc = models.IntegerField()
    
    # Video
    youtube_id = models.CharField(max_length=64)
    youtube_title = models.CharField(max_length=128)
    
    # Filtering
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=256)
    
    # Ratings
    ratings = models.IntegerField()
    total_stars = models.FloatField()

    def __str__(self):
        return self.name


class Rating(models.Model):
    """
    Represents a rating on an artist/band.
    """
    ip = models.CharField(max_length=36)
    value = models.FloatField()
