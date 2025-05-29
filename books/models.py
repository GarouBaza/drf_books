from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    city = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='user')


class Book(models.Model):
    genre_choices = [
        ('Give', 'Отдам'),
        ('Sell', 'Продам'),
        ('Occupied', 'Занято'),
    ]

    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.CharField(max_length=100, verbose_name='Имя автора')
    description = models.TextField(blank=True, null=True, verbose_name='Описание книги')
    genre = models.CharField(max_length=100, verbose_name='Жанр книги')
    status = models.CharField(choices=genre_choices, verbose_name='Статус книги')
    photo = models.ImageField(upload_to='books_photos/', verbose_name='Фото книги', blank=True, null=True)
    city = models.CharField(max_length=10, verbose_name='Откуда привезли книгу')
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE, blank=True,
                              related_name='books')

class Review(models.Model):
    rating = models.FloatField()
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)




