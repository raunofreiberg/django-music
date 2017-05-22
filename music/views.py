from django.views import generic
from .models import Album, Song


class IndexView(generic.ListView):
    model = Album
    template_name = 'music/index.html'
    context_object_name = 'all_albums'


class SongsView(generic.ListView):
    model = Song
    template_name = 'music/songs.html'
    context_object_name = 'all_songs'


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
