from django.shortcuts import render
from articles.models import Articles
from music.models import Song

def main(request):
    articles = []
    if request.user.is_authenticated:
        articles = Articles.objects.filter(user=request.user).order_by('-pk')
    context = {
        'articles':articles,
    }
    return render(request, 'main.html', context)
