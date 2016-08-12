from django.shortcuts import render
from django.utils import timezone
from .models import Song
from .forms import SongForm
from django.shortcuts import redirect


# Create your views here.
def song_list(request):
    songs = Song.objects.filter(added_date__lte=timezone.now()).order_by('added_date')
    return render(request, 'voting/song_list.html', {'songs': songs})


def add_song(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.added_date = timezone.now()
            song.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'voting/add_song.html', {'form': form})
