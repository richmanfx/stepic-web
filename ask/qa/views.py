# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from models import Question, Answer
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from forms import AskForm, AnswerForm, SignupForm, LoginForm


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


def question_popular(request):
    all_questions = Question.objects.all()
    sort_last_questions = all_questions.order_by('-rating')
    page_object, paginator = my_paginate(request, sort_last_questions)
    paginator.baseurl = '/popular/?page='
    
    return render(request, 'list_popular_page.html', {
	'page_object': page_object,
	'paginator': paginator,
    })

def question(request, q_id):
    # Получим объект модели с первичным ключом = q_id
    question = get_object_or_404(Question, pk=q_id)	# если плохой q_id, вернёт 404
    answers = Answer.objects.all()
    answers = Answer.objects.filter(question = question)
    
    return render(request, 'one_question_page.html', {
	'question': question,
	'answers': answers,
    })

################################################################

def ask_add(request):
    if request.method == 'POST':
	form = AskForm(request.POST)
	if form.is_valid():
	    question = form.save()
	    # url = question.get_url()
	    # return HttpResponseRedirect(reverse(url))
	    return HttpResponseRedirect(reverse('question', args=[question.id-1]))
    else:
	form = AskForm()
	
    return render(request, 'ask_add_page.html', {'form': form})
    
def answer_add(request):
    if request.method == 'POST':
	form = AnswerForm(request.POST)
	if form.is_valid():
	    answer = form.save()
	    url = question.get_url()
	    return HttpResponseRedirect(reverse(url))
    return HttpResponseRedirect('/')

#################################################################
'''
URL = /signup/
username - имя пользователя, логин
email - email пользователя
password - пароль пользователя

При GET запросе должна отображаться форма для ввода данных, при POST запросе создается 
новый пользователей, осуществляется вход (login) созданного пользователя на сайт, 
возвращается редирект на главную страницу.
'''


def signup(request):
    if request.method == 'POST':
	form = SignupForm(request.POST)
	if form.is_valid():
	    user = form.save()
	    login(request, user)
	    return HttpResponseRedirect('/')
    else:
	form = SignupForm()
    return render(request, 'signup_page.html', {'form': form})
    
    
'''
URL = /login/
username - имя пользователя
password - пароль пользователя
При GET запросе должна отображаться форма для ввода данных, при POST запросе 
происходит вход (login) на сайт, возвращается редирект на главную страницу. 
'''

def my_login(request):
    if request.method == 'POST':
	form = LoginForm(request.POST)
	if form.is_valid():
	    user = authenticate()
	    if user is not None:
		login(request, user)
		return HttpResponseRedirect('/')
    else:
	form = LoginForm()
    return render(request, 'login_page.html', {'form': form})
