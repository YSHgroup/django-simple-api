from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.TextField()
    completed = models.BooleanField(default=True)

    def __str__(self) :
        return self.name
