from django.contrib import admin

from books.models import Review, Book, CustomUser

# Register your models here.
admin.site.register(Review)
admin.site.register(Book)
admin.site.register(CustomUser)