from django.contrib import admin

from book.models import Author, Genre, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
        list_display = ('name', 'created_at', 'updated_at')
        search_fields = ('name',)
        list_filter = ('created_at', 'updated_at')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
        list_display = ('name', 'created_at', 'updated_at')
        search_fields = ('name',)
        list_filter = ('created_at', 'updated_at')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'price', 'created_at', 'updated_at')
        search_fields = ('title', 'genre__name', 'author__name')
        list_filter = ('genre', 'author')
