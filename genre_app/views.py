from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Genre
from .serializers import GenreSerializer
from .serializers import GenreViewSerializer
# Create your views here.
class GenreView(APIView):
    def get(self, request, genre_pk=None):
        if genre_pk is not None:
            genre = get_object_or_404(Genre, pk=genre_pk)
            serializer = GenreViewSerializer(genre)
        else:
            genres = Genre.objects.order_by('pk')
            serializer = GenreViewSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        genre = request.data
        serializer = GenreSerializer(data=genre)
        if serializer.is_valid(raise_exception=True):
            genre = serializer.save()
        return Response(f'{genre.name} created')
    
    def put(self, request, genre_pk):
        genre = get_object_or_404(Genre, pk=genre_pk)
        data = request.data
        serializer = GenreSerializer(instance=genre, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            genre = serializer.save()
        return Response(f'{genre.name} updated')
    
    def delete(self, request, genre_pk):
        genre = get_object_or_404(Genre, pk=genre_pk)
        name = genre.name
        genre.delete()
        return Response(f'{name} deleted')

