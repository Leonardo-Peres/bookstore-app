# Generated by Django 5.1.2 on 2024-11-01 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Autor'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name': 'Livro'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Gênero'},
        ),
    ]
