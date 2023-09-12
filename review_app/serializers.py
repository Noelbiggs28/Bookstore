from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Review
from book_app.models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title",)
    def to_representation(self, instance):
        return instance.title

class ReviewViewSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = Review
        fields = ("pk", 'book', 'rating', 'summary')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("pk", 'rating', 'summary')

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.save()
        return instance