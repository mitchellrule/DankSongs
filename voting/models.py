from django.db import models


class Song(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    votes = models.IntegerField(blank=True, null=True)

    def publish(self):
        votes = 0
        self.save()

    def __str__(self):
        return self.title
