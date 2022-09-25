t = int(input())
for _ in range(t):
    car = int(input())
    options = int(input())
    cnt = car
    for i in range(options):
        a,b = map(int,input().split())
        c = a*b
        cnt += c
    print(cnt)
