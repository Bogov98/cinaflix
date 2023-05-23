from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    vote_average = models.DecimalField(max_digits=3, decimal_places=1)
    release_date = models.DateField()
    imdb_id = models.CharField(max_length=100)
    generos = models.CharField(max_length=200)
    poster_link = models.URLField()

    def str(self):
        return self.title

class Vista(models.Model):
    idvista = models.AutoField(primary_key=True)
    idmovie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Vista {self.idvista}' 

class Comentario(models.Model):
    idcomentario = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=200)
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE)
    idmovie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentario {self.idcomentario}'      

class Favorito(models.Model):
    idfavorito = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE)
    idmovie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'Favorito {self.idfavorito}'                 