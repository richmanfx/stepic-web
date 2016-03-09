# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User, )
    likes = [User, ]

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    question = Question
    author = models.ForeignKey(User, )

    def __unicode__(self):
        return self.title
