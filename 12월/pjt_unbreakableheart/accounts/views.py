from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash
import requests
import json
from .models import *
from articles.models import *
from django.contrib import messages

# Create your views here.


def signup(request):
    # 이미 회원가입한 유저라면
    # if request.user.is_authenticated:
    #     return redirect("accounts:index")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(request.GET.get("next") or "main")
        else:
            form = CustomUserCreationForm()
            context = {
                "form": form,
                "validate": 1,
            }
            return render(request, "accounts/signup.html", context)
    else:
        form = CustomUserCreationForm()
        context = {
            "form": form,
            "validate": 0,
        }
        return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            message_d = MessageDeclaration.objects.filter(reported=request.user.pk)
            comment_d = CommentDeclaration.objects.filter(reported=request.user.pk)
            articles_d = ArticlesDeclaration.objects.filter(reported=request.user.pk)
            if len(message_d) + len(comment_d) + len(articles_d) >= 3:
                # 임시
                auth_logout(request)
                messages.warning(request, "정지된 계정입니다. 운영자에게 문의해주세요.")
                return redirect("main")
            else:
                return redirect(request.GET.get("next") or "main")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect("main")


@login_required
def update(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    if user == request.user:
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect("accounts:profile", user_pk)
        else:
            form = CustomUserChangeForm(instance=user)
        context = {
            "form": form,
        }
        return render(request, "accounts/update.html", context)
    else:
        return render(request, "main.html")


@login_required
def profile(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    articles = user.articles_set.filter(user=user.pk)
    message = Message.objects.filter(receiver_id=user.pk).order_by("-articles")
    feelings = Sympathy.objects.filter(user=user_pk)
    liked = []
    for article in feelings:
        for i in liked:
            if article.articles == i.articles:
                break
        else:
            liked.append(article)
    context = {
        "user": user,
        "articles": articles,
        "message": message,
        "feelings": len(liked),
    }
    return render(request, "accounts/profile.html", context)


@login_required
def message_receive(request):
    message = Message.objects.filter(receiver_id=request.user).order_by("-pk")

    if message:
        context = {
            "message": message,
            "message_declaration_form": MessageDeclarationForm(),
        }
    else:
        context = {
            "message": 1,
        }

    return render(request, "accounts/message_receive.html", context)


@login_required
def delete(request):
    user = get_user_model().objects.get(pk=request.user.pk)
    user.delete()
    return redirect("main")


# 비밀번호 변경
@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 로그인 유지
            update_session_auth_hash(request, request.user.pk)
            return redirect("accounts:profile", request.user.pk)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/password.html", context)


# 카카오 소셜 로그인
def kakao_request(reqeust):
    kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
    redirect_uri = "http://unbreakableheart-env.eba-fq3y3emz.ap-northeast-2.elasticbeanstalk.com/accounts/kakao/login/callback/"
    client_id = "fdc7989db5f7e970c9ba50edb78ec9a6"
    return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}")


def kakao_callback(request):
    data = {
        "grant_type": "authorization_code",
        "client_id": "fdc7989db5f7e970c9ba50edb78ec9a6",
        "redirect_uri": "http://unbreakableheart-env.eba-fq3y3emz.ap-northeast-2.elasticbeanstalk.com/accounts/kakao/login/callback/",
        "code": request.GET.get("code"),
    }

    kakao_token_api = "https://kauth.kakao.com/oauth/token"
    access_token = requests.post(kakao_token_api, data=data).json()["access_token"]

    headers = {"Authorization": f"bearer ${access_token}"}
    kakao_user_api = "https://kapi.kakao.com/v2/user/me"
    kakao_user_information = requests.get(kakao_user_api, headers=headers).json()
    kakao_id = kakao_user_information["id"]
    kakao_nickname = kakao_user_information["properties"]["nickname"]
    kakao_birthday = kakao_user_information["kakao_account"].get("birthday")

    # 받아온 kakao 유저정보중 id가 db에 있는지 확인합니다.
    if get_user_model().objects.filter(username=kakao_id).exists():
        kakao_user = get_user_model().objects.get(username=kakao_id)
        # kakao_user.refresh_token = temp["refresh_token"]
        kakao_user.save()
    else:
        kakao_login_user = get_user_model().objects.create(
            username=kakao_id,
            fullname=kakao_nickname,
            birthday=kakao_birthday,
            # refresh_token = temp["refresh_token"],
        )
        kakao_login_user.save()
        kakao_user = get_user_model().objects.get(username=kakao_id)
    auth_login(request, kakao_user, backend="django.contrib.auth.backends.ModelBackend")
    return redirect(request.GET.get("next") or "main")


@login_required
def message_create(request, user_pk, articles_pk):
    articles = Articles.objects.get(pk=articles_pk)
    receiver = User.objects.get(pk=user_pk)
    if request.method == "POST":
        message_form = MessageForm(request.POST)
        if message_form.is_valid:
            message = message_form.save(commit=False)
            message.sender = request.user
            message.receiver = receiver
            message.articles = articles
            if request.POST["song"]:
                song = Song.objects.get(song_title=request.POST["song"])
                message.song = song
            message.save()
            return redirect("articles:articles_detail", articles_pk)
    else:
        message_form = MessageForm()
    context = {
        "receiver": receiver,
        "message_form": message_form,
    }
    return render(request, "accounts/message_create.html", context)


@login_required
def message_delete(request):
    message = Message.objects.filter(receiver_id=request.user).order_by("-articles")
    if request.method == "POST":

        selected = request.POST.getlist("selected")
        print(selected)
        for m in message:
            for s in selected:
                if m.id == int(s):
                    m.delete()
    return redirect("accounts:message_receive")


@login_required
def message_delete_all(request):
    message = Message.objects.filter(receiver_id=request.user)
    message.delete()
    return redirect("accounts:message_receive")


def message_detail(request, message_pk):
    message = Message.objects.get(pk=message_pk)
    message.read = True
    message.save()
    context = {
        "message": message,
        "message_declaration_form": MessageDeclarationForm(),
    }
    return render(request, "accounts/message_detail.html", context)


# 메시지 신고
from django.db import IntegrityError


@login_required
def message_declaration(request, message_pk):
    message = Message.objects.get(pk=message_pk)
    if request.method == "POST":
        message_declaration_form = MessageDeclarationForm(request.POST)
        if message_declaration_form.is_valid():
            try:
                declaration = message_declaration_form.save(commit=False)
                declaration.reporter = request.user
                declaration.reported = message.sender
                declaration.message = message
                message_declaration_form.save()
                messages.warning(request, "신고되었습니다.")
                return redirect("accounts:message_detail", message_pk)
            except IntegrityError:
                messages.info(request, "이미 신고된 메시지입니다.")
                return redirect("accounts:message_detail", message_pk)
    else:
        message_declaration_form = MessageDeclarationForm()
    context = {
        "message_declaration_form": message_declaration_form,
    }
    return render(request, "accounts/message_receive.html", context)


def counter(request):
    count = 0
    try:
        if request.user.is_authenticated:
            message = Message.objects.filter(receiver=request.user)
            for m in message:
                if m.read == 0:
                    count += 1
        else:
            pass
    except Message.DoesNotExist:
        count = 0
    return {
        "count": count,
    }


def feeling_page(request):
    feelings = Sympathy.objects.filter(user=request.user).order_by("-pk")
    liked = []
    for article in feelings:
        for i in liked:
            if article.articles == i.articles:
                break
        else:
            liked.append(article)
    context = {
        "feelings": liked,
    }
    return render(request, "accounts/feeling_page.html", context)
