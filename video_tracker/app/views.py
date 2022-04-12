from django.shortcuts import render
from .models import Channel, Video
from django.conf import settings
import requests


def index(request):
    channels = Channel.objects.all()
    context = {'channels': channels}
    return render(request, 'index.html', context)


def channel_search(request):
    query = request.GET.get('q')
    url = f'https://www.googleapis.com/youtube/v3/search?q={query}&type=channel&part=snippet&key={settings.YOUTUBE_API_KEY}'
    res = requests.get(url)

    results = res.json()['items']
    context = {'results': results}
    return render(request, 'partials/channel_search_results.html', context)


def add_channel(request):
    """TODO: Add channel to database"""
    # 27:06 https://www.youtube.com/watch?v=vukzYCi2_yE&t=8s
    pass
