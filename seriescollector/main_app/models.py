from django.db import models

# Create your models here.
class Series(models.Model):
    title = models.CharField(max_length=100)
    seasons = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
