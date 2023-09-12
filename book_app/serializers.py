from rest_framework import serializers
from django.shortcuts import get_list_or_404
from .models import Book
from author_app.models import Author
from genre_app.models import Genre

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name','last_name')
    def to_representation(self, instance):
        return instance.last_name

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)
    def to_representation(self, instance):
        return instance.name

class BookViewSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer()
    class Meta:
        model = Book
        fields = ('pk', "title", "author", "genre")

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('pk', "title", "author", "genre")
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance