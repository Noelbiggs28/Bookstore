# Generated by Django 4.2.5 on 2023-09-11 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre_app', '0001_initial'),
        ('author_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='genre_app.genre'),
        ),
    ]
