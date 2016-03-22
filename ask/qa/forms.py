# -*- coding: utf-8 -*-
from django import forms
from models import Question, Answer
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login

'''
AskForm - форма добавления вопроса
title - поле заголовка
text - поле текста вопроса
'''
class AskForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок вопроса')
    text = forms.CharField(widget=forms.Textarea, label='Текст вопроса')

    def clean_title(self):
	title = self.cleaned_data['title']
	if title.strip() == '':
	    raise forms.ValidationError(
		u'Поле Заголовок вопроса не заполнено.'
	    )
	return title

    def clean_text(self):
	text = self.cleaned_data['text']
	if text.strip() == '':
	    raise forms.ValidationError(
		u'Поле Текст вопроса не заполнено.'
	    )
	return text

    def save(self):
	self.cleaned_data['author_id'] = 1
	question = Question(**self.cleaned_data)
	question.save()
	return question


'''
AnswerForm - форма добавления ответа
text - поле текста ответа
question - поле для связи с вопросом
'''
class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    
    def clean_text(self):
	text = self.cleaned_data['text']
	if text.strip() == '':
	    raise forms.ValidationError(
		u'Поле Текст ответа не заполнено.'
	    )
	return text
    
    def clean_question(self):    
	question = self.clean_data['question']
	if question:
	    raise forms.ValidationError(
		u'Требуется номер вопроса'
	    )
	return question
	
    def save(self):
	self.cleaned_data['author_id'] = 1
	answer = Answer(**self.cleaned_data)
	ansver.save()
	return answer

'''    
username - имя пользователя, логин
email - email пользователя
password - пароль пользователя
'''
class SignUp(forms.Form):
    username = forms.CharField(max_length='50')
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_username(self):
	username = self.cleaned_data['username']
	if username.strip() == '':
	    raise forms.ValidationError(
		u'Pole USERNAME pustoe!'
	    )
	return username

    def clean_email(self):
	email = self.cleaned_data['email']
	if email.strip() == '':
	    raise forms.ValidationError(
		u'Pole EMAIL pustoe!'
	    )
	return email
    
    
    def clean_password(self):
	password = self.cleaned_data['password']
	if password.strip() == '':
	    raise forms.ValidationError(
		u'Pole PASSWORD pustoe!'
	    )
	return password

    def save(self):
	user = User.objects.create_user(**self.cleaned_data)
	user.save()
	return authenticate(**self.cleaned_data)

