from django.db import models
from genre_app.models import Genre

# Create your models here.
class Author(models.Model):
    first_name=models.TextField()
    last_name=models.TextField()
    genres = models.ManyToManyField(Genre, blank=True)
    
    def __str__(self):
        return self.last_name
    
    def add_genre(self, genre):
        self.genres.add(genre)

    def remove_genre(self, genre):
        self.genres.remove(genre)