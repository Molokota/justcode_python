from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from geoposition.fields import GeopositionField

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)
    mobile_phone = models.CharField(verbose_name='Мобильный тел.', max_length=12, null=True, blank=True,)
    nickname = models.CharField(max_length=30, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True, default='accounts/img/user.png')    # фото пользователя
    objects = UserManager()

    # геопозиция
    position = GeopositionField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.id} --- {self.mobile_phone} --- {self.nickname} --- {self.email}'

    class Meta:
        db_table = 'users'
        ordering = ["-date_joined"]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'