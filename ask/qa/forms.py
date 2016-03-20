# -*- coding: utf-8 -*-
from django import forms
from models import Question, Answer

'''
AskForm - форма добавления вопроса
title - поле заголовка
text - поле текста вопроса
AnswerForm - форма добавления ответа
text - поле текста ответа
question - поле для связи с вопросом
'''

class AddAskForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок вопроса')
    text = forms.CharField(widget=forms.Textarea, label='Текст вопроса')

    def clean_title(self):
	title = self.cleaned_data['title']
	if title.strip() == '':
	    raise forms.ValidationError(
		u'Поле /"Заголовок вопроса/" не заполнено.'
	    )
	return title

    def clean_text(self):
	text = self.cleaned_data['text']
	if text.strip() == '':
	    raise forms.ValidationError(
		u'Поле /"Текст вопроса/" не заполнено.'
	    )
	return text

    def save(self):
	self.cleaned_data['author_id'] = 1
	question = Question(**self.cleaned_data)
	question.save()
	return question

'''
class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
#    question = forms    
'''    
    
    
    
    
    
    
    