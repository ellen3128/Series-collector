from django.db import models

# Create your models here.
class Series(models.Model):
    title = models.CharField(max_length=100)
    seasons = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()

#   {'title': 'You', 'seasons': 4, 'genre': 'Thriller', 'rating': 7.7 }, 
#   {'title': 'Money Heist', 'seasons': 5, 'genre': 'Thriller', 'rating': 8.2 }, 
#   {'title': 'Black Mirror', 'seasons': 6, 'genre': 'Sci-fi', 'rating': 8.7 }, 
#   {'title': 'Inventing Anna', 'seasons': 1, 'genre': 'Drama', 'rating': 6.8 }, 

def __str__(self):
    return self.name