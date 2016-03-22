from django.conf.urls import patterns, include, url
from qa.views import *

urlpatterns = patterns('',
    url(r'^$', question_list_all, name='question_list_all'),
    url(r'^popular/', question_popular, name='question_popular'),
    url(r'^question/(?P<q_id>\d+)/', question, name='question'),
    url(r'^ask/', ask_add, name='ask'),
    url(r'^answer/', answer_add, name='answer'),
    url(r'^signup/', signup, name='signup'),    
#    url(r'^login/', login, name='login'),
)