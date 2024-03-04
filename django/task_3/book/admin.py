from django.contrib import admin
from .models import Book, Author

# Register your models here.
@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display=('id', 'title')

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display=('id', 'name')
