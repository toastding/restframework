from rest_framework import viewsets
from musics.models import Music
from musics.serializers import MusicSerializer

# Create your views here.


class MusicViewSet(viewsets.ModelViewSet):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer
