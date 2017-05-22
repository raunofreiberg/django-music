from django.conf.urls import url
from . import views


urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/pk
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/songs
    url(r'^songs/$', views.SongsView.as_view(), name='songs'),
]
