from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.


def review(request):
    return render(request, "review/review.html")


def index(request):
    review = Review.objects.order_by("-pk")
    context = {"review": review}
    return render(request, "review/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect("review:index")
    else:
        review_form = ReviewForm()
    context = {"review_form": review_form}
    return render(request, "review/form.html", context=context)


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
