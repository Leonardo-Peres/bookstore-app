from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nome')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=80, verbose_name='Gênero')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Gênero'
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Autor')
    genre = models.ManyToManyField(Genre, verbose_name='gênero')
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    year_release = models.IntegerField(verbose_name='Ano de Lançamento')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Livro'
        ordering = ['title']

    def __str__(self):
        return self.title
