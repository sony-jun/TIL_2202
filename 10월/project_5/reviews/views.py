from urllib.error import HTTPError
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from accounts.views import login
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
import os


def reviews_article(request):
    reviews = Article.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, "reviewing/article.html", context)
    

@login_required
def reviews_create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('reviews:reviews-article')
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, "reviewing/create.html", context)

def reviews_detail(request, pk):
    form = Article.objects.get(pk=pk)
    comment = CommentForm()
    comments = form.comment_set.all()
    context = {
        'form' : form,
        'comment' : comment,
        'comments' : comments,
    }
    return render(request, 'reviewing/detail.html', context)

@login_required
def reviews_update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method=="POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                if (article.image and request.FILES.get('image')) or request.POST.get('image-clear'):
                    os.remove(article.image.path)
                if (article.image_thumbnail and request.FILES.get('thumbnail')) or request.POST.get('thumbnail-clear'):
                    os.remove(article.image_thumbnail.path)
                form.save()
                return redirect("reviews:reviews-detail", pk )
        else:
            form = ArticleForm(instance=article)
        context = {
            'form' : form,
            'article' : article,
        }
        return render(request, 'reviewing/update.html', context)
    else:
        return redirect("reviews:reviews-article")

@login_required
def reviews_delete(request, pk):
    if request.user == article.user:
        article = Article.objects.get(pk=pk)
        if article.image:
            os.remove(article.image.path)
        if article.image_thumbnail:
            os.remove(article.image_thumbnail.path)
        article.delete()
        return redirect('reviews:reviews-article')
    else:
        return redirect('reviews:reviews-article')

# comment 부분
def reviews_comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.article = article
                comment.user = request.user
                comment.save()
                context = {
                    'content' : comment.content,
                    'userName' : comment.user.username,
                }
                return JsonResponse(context)
        else:
            return HttpResponse(status=403)
    else:
        return redirect("accounts:login")