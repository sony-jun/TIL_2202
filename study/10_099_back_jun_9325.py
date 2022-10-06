t = int(input()) # 횟수
for _ in range(t):
    car = int(input()) # 차 가격
    options = int(input()) # 옵션의 개수
    cnt = car # 총 가격의 합이니까 기본값이 차 가격으로 설정
    for i in range(options): # 옵션의 개수가 0일 경우, for문이 돌아가지 않음
        a,b = map(int,input().split()) # 옵션개수, 옵션 가격 받음
        c = a*b # 두개 곱함
        cnt += c # 더해줌
    print(cnt) # 총 가격


'''
t = int(input())
for _ in range(t):
    car = int(input())
    bupum = int(input())
    if bupum ==0:
        print(car)
    else:
        mum = car
        for _ in range(bupum):
            a,b = map(int,input().split())
            c = a*b
            mum += c
        print(mum)
'''