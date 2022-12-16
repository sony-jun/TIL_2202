from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# search
import requests
from django.conf import settings
from isodate import parse_duration
from .forms import SongForm
from .models import Song

# Create your views here.
# search view start
def search(request):
    videos = []

    if request.method == "POST":
        search_url = "https://www.googleapis.com/youtube/v3/search"
        video_url = "https://www.googleapis.com/youtube/v3/videos"

        search_params = {
            "part": "snippet",
            "q": request.POST["search"],
            "key": settings.YOUTUBE_DATA_API_KEY,
            "maxResults": 6,
            "type": "video",
        }

        r = requests.get(search_url, params=search_params)
        results = r.json()["items"]

        video_ids = []
        for result in results:
            video_ids.append(result["id"]["videoId"])

        # if request.POST["submit"] == "lucky":
        #     return redirect(f"https://www.youtube.com/watch?v={ video_ids[0] }")

        video_params = {
            "key": settings.YOUTUBE_DATA_API_KEY,
            "part": "snippet,contentDetails",
            "id": ",".join(video_ids),
            "maxResults": 6,
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()["items"]

        for result in results:
            video_data = {
                "title": result["snippet"]["title"],
                "id": result["id"],
                "url": f'https://www.youtube.com/watch?v={ result["id"] }',
                "duration": 
                    parse_duration(result["contentDetails"]["duration"])
                ,
                "thumbnail": result["snippet"]["thumbnails"]["high"]["url"],
                "info":[result["snippet"]["title"],
                f'https://www.youtube.com/watch?v={ result["id"] }',
                result["snippet"]["thumbnails"]["high"]["url"],
                ]
            }

            videos.append(video_data)

    context = {
        "videos": videos,
    }
    # messages.success(request, "검색 결과입니다.")
    return render(request, "music/search.html", context)

# END Search
@login_required
def create(request):
    if request.method == 'POST':
        check = Song.objects.filter(song_url = request.POST['song_url'])
        if check:
            return HttpResponse('<script type="text/javascript">window.close()</script>')
        songform = SongForm(request.POST, request.FILES)
        if songform.is_valid():
            song = songform.save(commit=False)
            song.song_title = song.song_title.replace('\"', '\'')
            song.save()
    return HttpResponse('<script type="text/javascript">window.close()</script>')
