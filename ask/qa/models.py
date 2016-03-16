# -*- coding: utf-8 -*-
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)
    # author = models.ForeignKey(User)
    author = models.ForeignKey(User, related_name='question_autor')
    likes = models.ManyToManyField(User, related_name='question_likes')

    def __unicode__(self):
        return self.title

    #def get_absolute_url(self):
    def get_url(self):
	return reverse('question', kwargs={'id': self.id})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    #question = models.ForeingKey(Question)
    question = models.OneToOneField(Question)
    # author = models.ForeignKey(User)
    author = models.ForeignKey(User, related_name='answer_author')

    def __unicode__(self):
        return self.title

    def get_url(self):
	return reverse('question', kwargs={'id': self.id})
