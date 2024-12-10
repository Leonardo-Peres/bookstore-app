from dj_rql.filter_cls import AutoRQLFilterClass

from book.models import Author, Genre, Book


class AuthorFilterClass(AutoRQLFilterClass):
    MODEL = Author


class GenreFilterClass(AutoRQLFilterClass):
    MODEL = Genre


class BookFilterClass(AutoRQLFilterClass):
    MODEL = Book
    FILTERS = [
        {
            'filter': 'author',
            'source': 'author__name'
        },
        {
            'filter': 'genre',
            'source': 'genre__name'
        }
    ]