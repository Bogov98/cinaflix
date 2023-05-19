from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    vote_average = models.DecimalField(max_digits=3, decimal_places=1)
    release_date = models.DateField()
    imdb_id = models.CharField(max_length=100)
    generos = models.CharField(max_length=200)
    poster_link = models.URLField()

    def _str_(self):
        return self.title

# Create your models here.
