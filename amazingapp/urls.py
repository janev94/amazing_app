from django.conf.urls import patterns, url
from amazingapp import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/mazes$', views.mazes, name='mazes'),
)