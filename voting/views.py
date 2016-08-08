from django.shortcuts import render
from django.utils import timezone
from .models import Song

# Create your views here.
def song_list(request):
	songs = Song.objects.filter(added_date__lte=timezone.now()).order_by('added_date')
	return render(request, 'voting/song_list.html', {'songs': songs})
