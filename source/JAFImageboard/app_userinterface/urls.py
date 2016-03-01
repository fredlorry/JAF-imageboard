from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^(?P<tpc>[a-z]{2,3})$', views.threadlist, name='threadlist'),
    url(r'^(?P<tpc>[a-z]{2,3})/(?P<thr>\d{1,5})$', views.threadpage, name='threadpage'),
    url(r'.+$', views.homepage_redirect, name='redirect')
]