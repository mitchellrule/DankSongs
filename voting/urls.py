from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.song_list, name='song_list'),
    url(r'^add_song/$', views.add_song, name='add_song')
]
