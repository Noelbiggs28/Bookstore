from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Author
from genre_app.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("pk", "name")

    def to_representation(self, instance):
        return instance.name

class AuthorViewSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, required=False)
    class Meta:
        model = Author
        fields = ("pk","first_name","last_name", "genres")

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("pk","first_name","last_name", "genres")

    def create(self, data):
        author = Author.objects.create(first_name=data['first_name'], last_name=data['last_name'])
        if 'genres' in data:
            for genre in data['genres']:
                # genre_to_add = get_object_or_404(Genre, pk=genre)
                author.add_genre(genre)
        return author
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.genres.set(validated_data.get('genres',instance.genres.all()))
        instance.save()
        return instance

