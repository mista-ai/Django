from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=200, blank=True)
