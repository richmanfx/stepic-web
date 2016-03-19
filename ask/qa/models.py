# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='q_author', null=True)
    likes = models.ManyToManyField(User, related_name='q_likes', null=True)

    def __unicode__(self):
        return self.title

    def get_url(self):
        return reverse('question', kwargs={'id': self.id})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name='answer_set') 
    author = models.ForeignKey(User, related_name='a_authon', null=True)

    def __unicode__(self):
        return self.text

    def get_url(self):
        return reverse('answer', kwargs={'id': self.id})
