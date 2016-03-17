# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Question, Answer
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator


#####	test response
def test(request, *args, **kwargs):
    return HttpResponse('OK ')


#####	Главная страница
@require_GET			# Разрешить только GET- запросы
def main_page(request):
    # return HttpResponse('Отработала "main_page".')

    questions = Question.objects.all()		# получить все вопросы    
    questions = questions.order_by('-id')	# последний заданный вопрос - первый в списке
    

    return render(request, 'main_page.html', {'questions':	questions})

