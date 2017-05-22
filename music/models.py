from __future__ import unicode_literals
from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=500)
    artist = models.CharField(max_length=250)
    cover = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + ' - ' + self.artist + ', ' + self.genre


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=10)
    songTitle = models.CharField(max_length=250)    

    def __str__(self):
        return self.songTitle
