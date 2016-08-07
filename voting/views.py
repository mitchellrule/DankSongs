from django.shortcuts import render

# Create your views here.
def song_list(request):
	return render(request, 'voting/song_list.html')
