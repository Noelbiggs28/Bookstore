# Generated by Django 4.2.5 on 2023-09-11 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author_app', '0003_alter_author_genres'),
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='author_app.author'),
        ),
    ]
