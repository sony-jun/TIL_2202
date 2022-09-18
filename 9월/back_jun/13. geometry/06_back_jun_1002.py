t = int(input())
for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    mm = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    if mm == 0 and r1 == r2:
        print(-1)
    elif abs(r1-r2) == mm or r1 + r2 ==mm:
        print(1)
    elif abs(r1-r2) < mm < (r1+r2):
        print(2)
    else:
        print(0)