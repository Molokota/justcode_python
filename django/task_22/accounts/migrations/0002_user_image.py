# Generated by Django 4.2 on 2024-04-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='accounts/img/user.png', null=True, upload_to='img/'),
        ),
    ]
