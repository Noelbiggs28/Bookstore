from rest_framework import serializers

from .models import Genre
from author_app.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("last_name",)
    def to_representation(self, instance):
        return instance.last_name


class GenreViewSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, source ='author_set')
    class Meta:
        model = Genre
        fields = ("pk","name", 'authors')
    
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("pk","name")
    def create(self, validated_data):
        return Genre.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance