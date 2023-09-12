from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Review
from .serializers import ReviewViewSerializer
from .serializers import ReviewSerializer
from book_app.models import Book

class ReviewView(APIView):
    def get(self, request, book_pk, review_pk=None):
        if review_pk is not None:
            review = get_object_or_404(Review, pk=review_pk)
            serializer = ReviewViewSerializer(review)
        else:
            book = get_object_or_404(Book, pk=book_pk)
            reviews = book.review_set.all()
            serializer = ReviewViewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self, request, book_pk):
        review = request.data
        review['book'] = book_pk
        serializer = ReviewSerializer(data=review)
        if serializer.is_valid(raise_exception=True):
            review = serializer.save()
        return Response('review created')
    
    def put(self, request, book_pk, review_pk):
        review= get_object_or_404(Review, pk=review_pk)
        data = request.data
        serializer = ReviewSerializer(instance=review, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            review = serializer.save()
        return Response('review updated')
    
    def delete(self, request,book_pk, review_pk):
        review = get_object_or_404(Review, pk=review_pk)
        review.delete()
        return Response(f'review deleted')