from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Author
from .models import Genre
from .serializers import AuthorSerializer
from .serializers import AuthorViewSerializer


class AuthorView(APIView):
    def get(self, request, author_pk=None):
        if author_pk is not None:
            author = get_object_or_404(Author, pk=author_pk)
            serializer = AuthorViewSerializer(author)
        else:
            authors = Author.objects.order_by('pk')
            serializer = AuthorViewSerializer(authors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        author = request.data
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            author = serializer.save()
        return Response(f'{author.first_name} {author.last_name} created')
    
    def put(self, request, author_pk):
        author = get_object_or_404(Author, pk=author_pk)
        data = request.data   
        serializer = AuthorSerializer(instance=author, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            author = serializer.save()
        return Response(f'{author.first_name} {author.last_name} updated')
    
    def delete(self, request, author_pk):
        author = get_object_or_404(Author, pk=author_pk)
        name = f'{author.first_name} {author.last_name}'
        author.delete()
        return Response(f'{name} deleted')
