from django.db import models
from book_app.models import Book
from django.core import validators as v
# Create your models here.
class Review(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    rating=models.IntegerField(validators=[v.MinValueValidator(1,"Must be at least 1"), v.MaxValueValidator(10, "Can not exceed 10")])
    summary=models.TextField(max_length=255)