from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .models import Album, Song
from .forms import UserForm


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

            user = authenticate(username=username, password=password, first_name=first_name)

            if user != None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')
