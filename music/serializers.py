from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.Serializer):

    class Meta:
        model = Album
        fields = ('title', 'artist')
        # fields = '__all__'