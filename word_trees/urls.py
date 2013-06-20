# Create your views here.
from django.conf.urls import patterns, url

from word_trees import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<sentence_id>\d+)/$', views.detail, name='detail'),
)

