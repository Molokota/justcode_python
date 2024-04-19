from django.db import models
from accounts.models import User

class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name  

class Categories(models.Model):
    cat_name = models.CharField(max_length=128)

    def __str__(self):
        return f'id: {self.id} --- name: {self.cat_name}'

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    categories = models.ManyToManyField(Categories)
    title = models.CharField(max_length=255)    # заголовок
    genre = models.CharField(max_length=255, null=True)    # жанр книги
    image = models.ImageField(upload_to='img/', null=True)    # картинка обложки книги
    description = models.TextField(blank=True, null=True)    # описание книги

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')    # авто публикации
    time_created = models.DateTimeField(auto_now_add=True)    # дата созданий
    time_updated = models.DateTimeField(auto_now=True, null=True)    # дата последнего обновления записи
    is_published = models.BooleanField(default=True)    # True/False
    
    def get_absolute_url(self):
        return f"/post/{self.pk}/"
    
