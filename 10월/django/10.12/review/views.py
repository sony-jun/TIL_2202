from urllib import request
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.


def review(request):
    return render(request, "review/review.html")


def index(request):
    review = Review.objects.order_by("-pk")
    context = {"review": review}
    return render(request, "review/index.html", context)


def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
        return redirect("review:index")
    else:
        review_form = ReviewForm()
    context = {"review_form": review_form}

    return render(request, "review/create.html", context=context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)

    context = {"review": review}
    return render(request, "review/detail.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("review:index")
    else:
        review_form = ReviewForm(instance=review)
    context = {"review_form": review_form}
    return render(request, "review/update.html", context)


def delete(request, pk):
    Review.objects.get(id=pk).delete()
    return redirect("review:index")
