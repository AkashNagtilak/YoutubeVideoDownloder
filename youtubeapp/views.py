import os
import sys
from django.shortcuts import render
from pip._internal import resolution
from pytube import YouTube

url=''


def index(request):
    return render(request, 'youtubeapp/index.html')


def download(request):
    global url
    url = request.GET.get('url')
    yt = YouTube(url)
    video = []
    video = yt.streams.filter(progressive=True).all()
    embed_link = url.replace("watch?v=", "embed/")
    Title = yt.title
    context = {'video': video, 'embed': embed_link, 'title': Title}

    return render(request, 'youtubeapp/download.html', context)


def yt_download_done(request, resolution):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir = '/Downloads'

    if request.method == "POST":
        print('#########',url)
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        return render(request, 'youtubeapp/success.html')
    else:
        return render(request, 'youtubeapp/error.html')
