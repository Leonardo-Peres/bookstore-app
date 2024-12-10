from rest_framework import viewsets

from dj_rql.drf import RQLFilterBackend

from book.models import Author, Genre, Book
from book.serializers import AuthorSerializer, GenreSerializer, BookSerializer
from book.filters import AuthorFilterClass, GenreFilterClass, BookFilterClass


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    filter_backends = [RQLFilterBackend]
    rql_filter_class = AuthorFilterClass


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    filter_backends = [RQLFilterBackend]
    rql_filter_class = GenreFilterClass


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [RQLFilterBackend]
    rql_filter_class = BookFilterClass
