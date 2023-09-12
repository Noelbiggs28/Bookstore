from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Book
from author_app.models import Author
from genre_app.models import Genre
from .serializers import BookSerializer
from .serializers import BookViewSerializer


class BookView(APIView):
    def get(self, request, book_pk=None):
        if book_pk is not None:
            book = get_object_or_404(Book, pk=book_pk)
            serializer = BookViewSerializer(book)
        else:
            books = Book.objects.order_by("pk")
            serializer= BookViewSerializer(books, many=True)
        return Response (serializer.data)
    
    def post(self, request):
        book = request.data
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book = serializer.save()
        return Response(f'{book.title} created')
        
    def put(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book = serializer.save()
        return Response(f'{book.title} updated')
    
    def delete(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        name = f'{book.title}'
        book.delete()
        return Response(f'{name} deleted')
