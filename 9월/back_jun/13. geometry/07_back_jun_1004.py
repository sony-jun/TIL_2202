t = int(input())

for _ in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    s = int(input())
    cnt = 0
    for i in range(s):
        cx,cy,r = map(int,input().split())
        dis1 = (x1-cx)**2 + (y1-cy)**2
        dis2 = (x2-cx)**2 + (y2-cy)**2
        cr = r**2

        if cr > dis1 and cr > dis2:
            pass
        elif cr > dis1:
            cnt += 1
        elif cr > dis2:
            cnt += 1
    print(cnt)