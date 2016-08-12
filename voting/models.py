from django.db import models
from django.utils import timezone
from vote.managers import VotableManager


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    added_date = models.DateTimeField(blank=True, null=True)
    votes = VotableManager()

    def publish(self):
        self.added_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
