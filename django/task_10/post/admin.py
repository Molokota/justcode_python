from django.contrib import admin
from .models import Post, Author


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display=('id', 'title', 'is_published')


    # Сортировка
    # readonly_fields = [
    #     'time_created',
    #     'time_updated'
    # ]
    # Поиск 
    search_fields = ['title']

    # Фильтр
    list_filter = ['is_published']


# admin.site.register(Post)
# admin.site.register(Author)


@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display=('id', 'name')


