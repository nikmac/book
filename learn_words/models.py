from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    text = models.TextField()


class Word(models.Model):
    users = models.ManyToManyField(User, related_name='words')
    articles = models.ManyToManyField(Article, related_name='words')
    learned = models.BooleanField(default=False)
