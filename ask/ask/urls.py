from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


urlpatterns = patterns('',
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', 'qa.views.main_page', name='main_page'),
    url(r'^$', 'qa.views.question_list_all', name='question_list_all'),
#    url(r'^question/(?P<id>\d+)/$', views.post_details, name='post_details'),
)
