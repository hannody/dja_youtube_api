from .views import index, channel_search
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('channelsearch/', channel_search, name='channel-search'),
]
