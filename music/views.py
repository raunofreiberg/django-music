from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import UserForm
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
    # asd
    model = Album
    template_name = 'music/album_create.html'
    fields = ['title', 'genre', 'artist', 'cover']


class DeleteAlbum(DeleteView):
    model = Album
    template_name = 'music/index.html'
    success_url = reverse_lazy('index')


class EditAlbum(UpdateView):
    model = Album
    template_name = 'music/album_edit.html'
    fields = ['title', 'genre', 'artist', 'cover']


class AddSong(CreateView):
    model = Song
    template_name = 'music/song_create.html'
    fields = ['songTitle']

    def form_valid(self, form):
        form.instance.album_id = self.kwargs.get('pk')
        return super(AddSong, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.album.pk})


class DeleteSong(DeleteView):
    model = Song
    template_name = 'music/detail.html'
    fields = ['songTitle']

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.album.pk})

# Not sure about this


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # normalize data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,
                                password=password, first_name=first_name)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')
