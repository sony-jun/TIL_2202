from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    review = Review.objects.all()

    context = {
        "review": review,
    }
    return render(request, "re_pair/index.html", context)


def detail(request, pk_):
    review = Review.objects.get(pk=pk_)
    context = {
        "review": review,
    }
    return render(request, "re_pair/detail.html", context)


def new(request):
    return render(request, "re_pair/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Review.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }

    return redirect("re_pair:index")


def edit(request, pk_):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    review = Review.objects.get(pk=pk_)
    context = {
        "review": review,
    }
    return render(request, "re_pair/edit.html", context)


def update(request, pk_):
    review = Review.objects.get(pk=pk_)

    title_ = request.GET.get("title")
    content_ = request.GET.get("content")

    review.title = title_
    review.content = content_

    review.save()

    return redirect("re_pair:detail", review.pk)


def delete(request, pk):
    Review.objects.get(id=pk).delete()
    return redirect("re_pair:index")
