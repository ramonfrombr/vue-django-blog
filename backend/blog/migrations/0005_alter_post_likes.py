# Generated by Django 4.0.2 on 2023-05-07 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
