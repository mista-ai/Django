# Generated by Django 4.2.6 on 2023-10-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_actor_delete_actors_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movie_app.actor'),
        ),
    ]
