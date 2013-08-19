# Create your views here.
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from word_trees import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<word_id>\d+)/$', views.detail, name='detail'),
)

urlpatterns += staticfiles_urlpatterns()
