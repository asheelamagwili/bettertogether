# Generated by Django 2.2.6 on 2019-12-08 08:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_remove_whiteboard_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='whiteboard',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
