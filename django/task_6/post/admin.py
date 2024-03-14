from django.contrib import admin
from .models import Post, Author


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display=('id', 'title')

# admin.site.register(Post)
# admin.site.register(Author)


@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display=('id', 'name')
