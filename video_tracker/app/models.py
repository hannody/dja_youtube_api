from turtle import title
from django import views
from django.db import models

class Channel(models.Model):
    name=models.CharField(max_length=255)
    playlist_id = models.CharField(max_length=255)
    thumbnail_url = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Video(models.Model):
    title = models.CharField(max_length=255)
    views = models.IntegerField()
    likes = models.IntegerField()
    youtube_id = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)