from django.db import models

# Create your models here.

class Genre(models.Model):
    name=models.TextField(max_length=30)

    def get_authors(self):
        return self.author_set.all()