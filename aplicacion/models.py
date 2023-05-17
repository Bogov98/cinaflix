from django.db import models

class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)





