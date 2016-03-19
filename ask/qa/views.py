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

    all_questions = Question.objects.all()		# получить все вопросы    
    #question = Question.objects.get(id=0)
    all_questions = all_questions.order_by('-id')	# последний заданный вопрос - первый в списке
    questions = all_questions[0:5]			# срез
    #qa = Question.objects.create(title='First question')
    #qa.text='eto pervy vopros.'
    #qa.save()
    return render(request, 'main_page.html', {'questions':	questions})


def my_paginate(request, query_set):
    try:
	limit = int(request.GET.get('limit', 10))
    except ValueError:
	limit = 10
    
    if limit > 100:
	limit = 10
	
    try:
	page = int(request.GET.get('page', 1))
    except ValueError:
	raise Http404

    paginator = Paginator(query_set, limit)
    
    try:
	page = paginator.page(page)
    except EmptyPage:
	page = paginator.page(paginator.num_pages)

    return page, paginator


def question_list_all(request):
    all_questions = Question.objects.all()
    sort_last_questions = all_questions.order_by('-id')
    #questions = sort_last_questions[0:1000]
    #limit = request.GET.get('limit', 10)
    # page = request.GET.get('page', 1)
    #paginator = Paginator(questions, limit)
    
    #page_object = paginator.page(page)
    
    page_object, paginator = my_paginate(request, sort_last_questions)
    paginator.baseurl = '/?page='
    
    return render(request, 'list_all_page.html', {
	'page_object': page_object,
	'paginator': paginator,
    })

