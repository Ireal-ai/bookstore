from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, generics

from product.filters import GenreAndPriceFilter
from product.models import Book, Genre, Comment
from product.serializer import BookSerializer, GenreSerializer, CommentSerializer, RatingSerializer
import random


# Create your views here.
class GenreView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']

    def get(self, request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response({'genres': serializer.data})


class CreateRatingView(generics.CreateAPIView):
    serializer_class = RatingSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            rating = serializer.save()
            return Response({'rating': str(RatingSerializer(rating))})
        else:
            return Response({'invalid': 'Invalid rating'})


class OneBookView(APIView):
    def get(self, request, id):
        queryset = Book.objects.get(pk=self.kwargs['id'])
        serializer = BookSerializer(queryset)
        return Response({"book": serializer.data})


class OneGenreView(APIView):

    def get(self, request, id):
        queryset = Genre.objects.get(pk=self.kwargs['id'])
        serializer = GenreSerializer(queryset)
        return Response({'genre': serializer.data})


class BookVS(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['price', 'title']
    search_fields = ['price', 'title']
    ordering_fields = ['title', 'id']
    ordering = ['title']

    # def list(self, request):
    #     queryset = Book.objects.all()
    #     serializer = BookSerializer(queryset, many=True)
    #     return Response(serializer.data)


class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = GenreAndPriceFilter
    filterset_fields = ['price', 'title', 'comments__id', 'genre__id']
    search_fields = ['price', 'title', 'comments__text']
    ordering_fields = ['title', 'id', 'price', 'author', 'date_of_issue', 'average_rate']
    ordering = ['title', 'price', 'author', 'date_of_issue', 'average_rate']

    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['genre', 'comments', 'price']
    # search_fields = ['=genre', 'comments', 'price']

    def get(self, request):
        books_qs = self.filter_queryset(Book.objects.all())
        serializer = BookSerializer(books_qs, many=True)
        # the many param informs the serializer that it will be serializing more than a single article.
        return Response({"books": serializer.data})


class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save()
            return Response({'comment': CommentSerializer(comment).data})
        else:
            return Response({'invalid': 'Invalid comment'})


class RecommendationView(generics.ListAPIView):

    def get(self, request):
        books = Book.objects.all()
        # [book.id for book in Book.objects.all()]
        while True:
            book1 = random.choice(books)
            book2 = random.choice(books)
            if book1 != book2:
                recommendation1 = BookSerializer(book1)
                recommendation2 = BookSerializer(book2)
                break

        return Response({
            'First recommendations': recommendation1.data,
            'Second recommendations': recommendation2.data
                            })
