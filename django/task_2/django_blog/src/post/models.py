from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    photo = models.ImageField('post/imgs/', null=True)
