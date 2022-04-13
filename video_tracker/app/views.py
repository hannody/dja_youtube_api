# Django
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Support libraries
import requests

# Local - Django
from .models import Channel


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

@csrf_exempt
def add_channel(request, channel_id):
    url = f'https://www.googleapis.com/youtube/v3/channels?id={channel_id}&part=snippet,contentDetails&key={settings.YOUTUBE_API_KEY}'
    res = requests.get(url)
    result = res.json()['items'][0]

    channel = Channel(
        name=result['snippet']['title'],
        playlist_id=result['contentDetails']['relatedPlaylists']['uploads'],
        thumbnail_url=result['snippet']['thumbnails']['default']['url'],
        description=result['snippet']['description']
    )

    channel.save()

    channels = Channel.objects.all()
    context = {'channels': channels}
    return render(request, 'partials/channels.html', context)


# https://www.youtube.com/watch?v=vukzYCi2_yE&t=8s
# 35:43