from django.shortcuts import render, redirect
from .models import Practice
from .forms import PracticeForm

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져와서..
    practice = Practice.objects.order_by("-pk")
    # Template에 전달한다.
    context = {"practice": practice}
    return render(request, "practice/index.html", context)


def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        practice_form = PracticeForm(request.POST)
        if practice_form.is_valid():
            practice_form.save()
            return redirect("practice:index")
    else:
        practice_form = PracticeForm()
    context = {"practice_form": practice_form}
    return render(request, "practice/new.html", context=context)


def detail(request, pk):
    # 특정 글을 가져온다.
    practice = Practice.objects.get(pk=pk)
    # template에 객체 전달
    context = {"practice": practice}
    return render(request, "practice/detail.html", context)


def update(request, pk):
    practice = Practice.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        practice_form = PracticeForm(request.POST, instance=practice)
        if practice_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            practice_form.save()
            return redirect("practice:detail", practice.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 practice_form을 랜더링
    else:
        # GET : Form을 제공
        practice_form = PracticeForm(instance=practice)
    context = {"practice_form": practice_form}
    return render(request, "practice/update.html", context)


def delete(request, pk):
    Practice.objects.get(id=pk).delete()
    return redirect("re_pair:index")
