from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name='homepage'),
    url(r'^(?P<tpc>[a-z]{2,3})/{0,1}$', views.ThreadlistView.as_view(), name='threadlist'),
    url(r'^(?P<tpc>[a-z]{2,3})/(?P<thr>\d{1,5})/{0,1}$', views.ThreadpageView.as_view(), name='threadpage'),
    url(r'.+$', views.RedirectToHomepage.as_view())
]