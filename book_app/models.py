from django.db import models
from author_app.models import Author
from genre_app.models import Genre

# Create your models here.
class Book(models.Model):
    title=models.TextField(max_length=50)
    author=models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    genre=models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)