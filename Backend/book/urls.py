from django.urls import path, include

from rest_framework.routers import DefaultRouter

from book.views import AuthorViewset, GenreViewset, BookViewset

router = DefaultRouter()
router.register('authors', AuthorViewset)
router.register('genres', GenreViewset)
router.register('books', BookViewset)

urlpatterns = [
    path('', include(router.urls))
]