from django.conf.urls import url
from . import views


urlpatterns = [
    
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /register/

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /music/pk
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/songs
    url(r'^songs/$', views.SongsView.as_view(), name='songs'),

    # /music/create
    url(r'^create/$', views.CreateAlbum.as_view(), name='create'),

    # /music/delete
    url(r'^/(?P<pk>[0-9]+)/delete$', views.DeleteAlbum.as_view(), name='delete'),

    # /music/edit
    url(r'^edit/(?P<pk>[0-9]+)/$', views.EditAlbum.as_view(), name='edit'),

    # /music/pk/addsong
    url(r'^(?P<pk>[0-9]+)/addsong$', views.AddSong.as_view(), name='addsong'),

]
