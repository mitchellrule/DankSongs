from django.db import models
from django.utils import timezone


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    votes = models.IntegerField(blank=True, null=True)
    added_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.votes = 0
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
