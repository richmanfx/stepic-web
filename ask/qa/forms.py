# -*- coding: utf-8 -*-
from django import forms
from models import Question, Answer

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
    

    
    
    