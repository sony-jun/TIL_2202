from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "index.html")


def ping(request):
    return render(request, "ping.html")


def pong(request):
    #    ball = request.GET.get('ball')
    #    context = {
    #        'name' : ball,
    #    }

    return render(request, "pong.html", {"name": request.GET.get("ball")})


def is_odd_even(request, _num):

    if _num == 0:
        te = "0"
    elif _num % 2 == 1:
        te = "홀수"
    elif _num % 2 == 0:
        te = "짝수"
    context = {"num": _num, "te": te}
    return render(request, "is-odd-even.html", context)


def calculate(request, first, second):

    cnt = first + second
    minus = first - second
    mum = first * second
    divide = first // second

    context = {
        "first": first,
        "second": second,
        "cnt": cnt,
        "minus": minus,
        "mum": mum,
        "divide": divide,
    }

    return render(request, "calculate.html", context)


def junsangin(request):
    return render(request, "junsangin.html")


def junsangout(request):
    junsang = request.GET.get("junsang")
    yourjun = [
        "아이리스",
        "클라우드",
        "바츠",
        "티파",
        "티나",
        "로크",
        "에드가",
        "매쉬",
        "샛져",
        "고양이",
        "강아지",
        "거북이",
        "토끼",
        "뱀",
        "사자",
        "호랑이",
        "표범",
        "치타",
        "하이에나",
        "기린",
        "코끼리",
        "코뿔소",
        "하마",
        "악어",
        "펭귄",
        "부엉이",
        "올빼미",
        "곰",
        "돼지",
        "소",
        "닭",
        "독수리",
        "타조",
        "고릴라",
        "오랑우탄",
        "침팬지",
        "원숭이",
        "코알라",
        "캥거루",
        "고래",
        "상어",
        "칠면조",
        "직박구리",
        "쥐",
        "청설모",
        "메추라기",
        "앵무새",
        "삵",
        "스라소니",
        "판다",
        "오소리",
        "오리",
        "거위",
        "백조",
        "두루미",
        "고슴도치",
        "두더지",
        "우파루파",
        "맹꽁이",
        "너구리",
        "개구리",
        "두꺼비",
        "카멜레온",
        "이구아나",
        "노루",
        "제비",
        "까치",
        "고라니",
        "수달",
        "당나귀",
        "순록",
        "염소",
        "공작",
        "바다표범",
        "들소",
        "박쥐",
        "참새",
        "물개",
        "바다사자",
        "살모사",
        "구렁이",
        "얼룩말",
        "산양",
        "멧돼지",
        "카피바라",
        "도롱뇽",
        "북극곰",
        "퓨마",
        "미어캣",
        "코요테",
        "라마",
        "딱따구리",
        "기러기",
        "비둘기",
        "스컹크",
        "돌고래",
        "까마귀",
        "매",
        "낙타",
        "여우",
        "사슴",
        "늑대",
        "재규어",
        "알파카",
        "양",
        "다람쥐",
        "담비",
    ]
    your = random.choice(yourjun)
    context = {"junsang": junsang, "your": your}

    return render(request, "junsangout.html", context)


def loremin(request):
    return render(request, "loremin.html")


def loremout(request):
    mundan = request.GET.get("mundan")
    dango = request.GET.get("dango")
    lorems = [
        "두더지",
        "우파루파",
        "맹꽁이",
        "너구리",
        "개구리",
        "두꺼비",
        "카멜레온",
        "이구아나",
        "노루",
        "제비",
        "까치",
        "고라니",
        "수달",
        "당나귀",
        "순록",
        "염소",
        "공작",
        "바다표범",
        "들소",
        "박쥐",
        "참새",
        "물개",
        "바다사자",
        "살모사",
        "구렁이",
        "얼룩말",
        "산양",
    ]
    cnt = int(dango)
    t = int(mundan)
    d = [random.choice(lorems) for i in range(cnt)]
    re = t * [d]

    context = {"mundan": mundan, "dango": dango, "d": d, "cnt": cnt, "t": t, "re": re}
    return render(request, "loremout.html", context)
