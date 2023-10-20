from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()

    def __str__(self):
        return f'title = {self.title}, rating = {self.rating}'
