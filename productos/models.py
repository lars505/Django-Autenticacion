from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre