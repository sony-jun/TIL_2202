from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import User
from products.models import Product, Image
from .forms import CustomUserAuthenticationForm
from django.http import JsonResponse

# 알림 메세지
from django.contrib import messages

# 이메일 회원가입 관련 메서드
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

# tokens.py 가져오기
from .tokens import account_activation_token

# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


def signup(request):
    # 이미 로그인된 사람은 accounts:index 로 보내기
    if request.user.is_authenticated:
        return redirect("accounts:index")
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST, request.FILES)
            if form.is_valid():
                # 바로 저장 안 하고 user 객체 받아옴
                user = form.save(commit=False)
                # user의 is_active(인증 여부)를 False로 저장 (default : True)
                user.is_active = False
                # user 정보 저장
                user.save()
                # "이메일 보내기 함수" 만들어서 정보 전달 (request, user 객체, 검증된 데이터["email"])
                activateEmail(request, user, form.cleaned_data.get("email"))
                return redirect("accounts:index")
            else:
                # error 발생하면 error 내용을 알림으로 띄움
                for err in list(form.errors.values()):
                    messages.error(request, err)
        else:
            form = CustomUserCreationForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/signup.html", context)


# 이메일 보내기 함수
# 1. signup form에서 받은 정보를 암호화
# 2. accounts/template_activate_account.html에 정보 전달
# 3. activateEmail()과 tokens.py의 정보를 받은 accounts/template_activate_account.html 양식으로, user.email에게 accounts:activate 링크로 연결되는 메일 보냄
def activateEmail(request, user, to_email):
    # 메일 제목
    mail_subject = "Activate your user account."
    # user 정보(+암호화) 전달 -> accounts/template_activate_account.html
    message = render_to_string(
        "accounts/template_activate_account.html",
        {
            "user": user.username,
            "domain": "http://para-env.eba-ezj4wh6p.ap-northeast-2.elasticbeanstalk.com/",
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": "https" if request.is_secure() else "http",
        },
    )
    # 이메일 전송 (제목, 내용, 보낼 곳)
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(
            request,
            f"<b>{user}</b>님, 고객님의 <b>{to_email}</b>로 가입 인증 링크를 전송 완료 했습니다. \
            메일에 들어가셔서 인증을 완료해주세요. <b>Note:</b> 메일함에 메일이 도착하지 않았다면 스팸 메일함을 확인해주세요.",
        )
    else:
        # 에러 처리
        messages.error(
            request,
            f"{to_email}로 메일을 전송하는데 실패하였습니다. 정확하게 이메일을 작성하였는지 확인해주세요.",
        )


# user 정보 복호화 및 인증 함수
# 1. user 정보 복호화
# 2. 복호화된 pk 값으로 user 객체 찾음
# 3. 찾은 user 객체를 is_active=True로 인증시킴
# 4. 로그인 후 accounts:index로 redirect
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request,
            f"이메일 인증이 완료되었습니다. <b>{user}</b>님 PARA에 오신 것을 환영합니다!",
        )
        auth_login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return redirect("accounts:index")
    else:
        messages.error(request, "링크가 유효하지 않습니다.")

    return redirect("accounts:main")


def detail(request, pk):
    images = Image.objects.all()

    user = get_user_model().objects.get(pk=pk)
    user_likes = user.like_restaurants.all()  # user가 찜하기 한 product 객체 리스트

    review_all = user.review_set.all()

    reviews = []  # 중복 제거한 리뷰 리스트
    reviews_id_check = []
    for review in review_all:
        if review.product_id not in reviews_id_check:
            reviews_id_check.append(review.product_id)
            reviews.append(review)

    imgs = [] # 중복 제거 + 내가 쓴 리뷰의 product의 첫 번째 이미지
    for review in reviews:
        imgs.append(Image.objects.filter(product_id=review.product_id)[0])

    context = {"user": user, "user_likes": user_likes, "reviews": reviews, "imgs": imgs}
    return render(request, "accounts/detail.html", context)


def login(request):
    # if request.user.is_anonymous:
    if request.method == "POST":
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        form = CustomUserAuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


# else:
#     return redirect("accounts:index")


def logout(request):
    auth_logout(request)
    return redirect("accounts:index")


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


def follow(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(pk=pk)
        if user != request.user:
            if user.followers.filter(pk=request.user.pk).exists():
                user.followers.remove(request.user)
                is_followed = False
            else:
                user.followers.add(request.user)
                is_followed = True
            follow_user = user.followers.filter(pk=request.user.pk)
            following_user = user.followings.filter(pk=request.user.pk)
            follow_user_list = []
            following_user_list = []
            for follow in follow_user:
                follow_user_list.append(
                    {
                        "pk": follow.pk,
                        "username": follow.username,
                    }
                )
            for following in following_user:
                following_user_list.append(
                    {
                        "pk": following.pk,
                        "username": following.username,
                    }
                )
            context = {
                "is_followed": is_followed,
                "follow_user": follow_user_list,
                "following_user": following_user_list,
                "followers_count": user.followers.count(),
                "followings_count": user.followings.count(),
            }
            return JsonResponse(context)
        return redirect("accounts:detail", user.username)
    return redirect("accounts:login")
