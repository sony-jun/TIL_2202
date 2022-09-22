from django.shortcuts import render
import random
# Create your views here.
def index(request):
    # 환영하는 메인 페이지를 보여준다.
    names = ['손희준','클라우드','바츠','티파','티나','로크']
    name = random.choice(names)
    context = {
        #변수명 : 값
        'name' : name,
        'img' : 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg'
    }
    return render(request, 'index.html', context)


def welcome(request, name):
        # 사람들이 /welcome/본인이름을 입력하면, 환영인사와 이름을 동시에 보여준다.
    context = {
        'name':name,
    }
    return render(request, 'welcome.html', context)
def today(request):
    menuS = ['짜장면','짬뽕','치킨','삼겹살','제육볶음','돈까스','초밥','김치찌개','된장찌개']
    menu = random.choice(menuS)
    
    if menu == '짜장면':
        img = 'https://upload.wikimedia.org/wikipedia/commons/e/e9/Korean.cuisine-Jajangmyeon-01.jpg'
    elif menu == '짬뽕':
        img = 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Jjamppong.jpg'
    elif menu =='치킨':
        img = 'https://upload.wikimedia.org/wikipedia/commons/2/20/Korean_fried_chicken_3_banban.jpg'
    elif menu =='삼겹살':
        img = 'https://upload.wikimedia.org/wikipedia/commons/b/b4/Samgyeopsal_%28pork_belly%29.jpg'
    elif menu =='제육볶음':
        img = 'https://upload.wikimedia.org/wikipedia/commons/6/65/%EC%A0%9C%EC%9C%A1_%EB%B3%B6%EC%9D%8C.jpg'    
    elif menu =='돈까스':
        img = 'https://upload.wikimedia.org/wikipedia/commons/d/d5/Tonkatsu_of_Kimukatsu.jpg' 
    elif menu =='초밥':
        img = 'https://upload.wikimedia.org/wikipedia/commons/f/f5/Sushi_at_restaurant_Itsudemo.jpg' 
    elif menu =='김치찌개':
        img = 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Korean_stew-Kimchi_jjigae-01.jpg' 
    elif menu =='된장찌개':
        img = 'https://upload.wikimedia.org/wikipedia/commons/a/a5/Doenjang_jjigae.jpg' 
    context = {
        'menu' : menu,
        'img' : img
    }

    return render(request, 'today-dinner.html',context)


def lotto(request):
    lotto_ = []
    thisweek = [3,11,15,29,35,44]
    
    for i in range(5):
        li = random.sample(range(1,45),6)
        lo = sorted(li)
        me = ''
        cnt = 0
        for k in thisweek:
            if k in li:
                cnt +=1
        if cnt == 6:
            me = '축하합니다!!! 1등입니다!'
        elif cnt == 5:
            if 10 in li:
                me = '축하합니다!! 하지만 조금 아쉬울지도??? 2등입니다'
            else:
                me = '축하합니다!! 3등입니다'
        elif cnt == 4:
            me = '4등입니다!'
        elif cnt == 3:
            me = '5등입니다'
        else:
            me = '꽝입니다 다음 기회에...'

        lotto_.append(lo)
   


        
        

    context = {
        'lotto' : lotto_,
        'message' : me
    }

    return render(request, 'lotto.html',context)