# Generated by Django 3.1.1 on 2020-11-22 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_game_clip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='clip',
        ),
    ]
