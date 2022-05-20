# Generated by Django 4.0.4 on 2022-05-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_user_media_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='media_choice',
        ),
        migrations.AddField(
            model_name='user',
            name='is_webd',
            field=models.BooleanField(default=False, verbose_name='Web Developer'),
        ),
    ]
