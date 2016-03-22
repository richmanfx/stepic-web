from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('qa.urls')),
#    url(r'^$', 'qa.views.main_page', name='main_page'),
#    url(r'^$', 'qa.views.question_list_all', name='question_list_all'),
#    url(r'^popular/', 'qa.views.question_popular', name='question_popular'),
#    url(r'^question/(?P<q_id>\d+)/', 'qa.views.question', name='question'),
#    url(r'^ask/', 'qa.views.ask_add', name='ask'),
#    url(r'^answer/', 'qa.views.answer_add', name='answer'),
#    url(r'^signup/', 'qa.views.signup', name='signup'),

)
