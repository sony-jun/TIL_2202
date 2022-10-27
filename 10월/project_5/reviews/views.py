from django.shortcuts import redirect, render
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def reviews_article(request):
    reviews = Article.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, "reviewing/article.html", context)
    
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
    context = {
        'form' : form,
    }
    return render(request, 'reviewing/detail.html', context)

def reviews_update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method=="POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
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
        return redirect("reivews:reviews-article")

def reviews_delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('reviews:reviews-article')
