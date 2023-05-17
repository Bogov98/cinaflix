from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass # Django ya incluye campos para el manejo de usuarios

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    duration_minutes = models.IntegerField()
    description = models.TextField()

class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class UserMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)


