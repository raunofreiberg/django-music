from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Album, Song


class IndexView(generic.ListView):
    model = Album
    template_name = 'music/index.html'
    context_object_name = 'all_albums'


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class SongsView(generic.ListView):
    model = Song
    template_name = 'music/songs.html'
    context_object_name = 'all_songs'


class CreateAlbum(CreateView):
    model = Album
    template_name = 'music/album_create.html'
    fields = ['title', 'genre', 'artist', 'cover']


class DeleteAlbum(DeleteView):
    model = Album
    template_name = 'music/album_delete.html'
    success_url = reverse_lazy('index')


class EditAlbum(UpdateView):
    model = Album
    template_name = 'music/album_edit.html'
    fields = ['title', 'genre', 'artist', 'cover']
