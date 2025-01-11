from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50, null=False)
    MOVIE_TYPE = {
        ('T', 'Terror'),
        ('C', 'Comedia'),
        ('F', 'Ciencia Ficción'),
        ('R', 'Romance'),
        ('A', 'Acción'),
        ('N', 'Animada'),
        ('H', 'Horror'),
        ('B', 'Basada en hechos reales'),
        ('I', 'Intriga'),
    }
    type = type = models.CharField(max_length=30, choices=MOVIE_TYPE, null= False)
    director_name = models.CharField(max_length=30, null=False)
    old = models.DateField()
    synopsis = models.TextField(max_length=200, null=False)
    
    def __str__(self)-> str:
        return f'{self.title} - {self.old}'
    

    