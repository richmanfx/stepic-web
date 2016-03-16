# -*- coding: utf-8 -*-
# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)

    author = models.ForeignKey(User, related_name='question_author')
    likes = models.ManyToManyField(User, related_name='question_likes')

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    question = models.OneToOneField(Question)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.text
