from django.db import models


# Create your models here.
class PostGato(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to="media/gatos")
    fecha_recate = models.DateField()

    def __str__(self):
        return self.titulo


class PostPerro(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to="media/perros")
    fecha_recate = models.DateField()

    def __str__(self):
        return self.titulo