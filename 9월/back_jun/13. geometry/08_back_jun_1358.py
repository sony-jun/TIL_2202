w,h,x,y,p = map(int, input().split())
cnt = 0
for _ in range(p):
    x1,y1 = map(int,input().split())
    # 중심점에서 거리를 재고
    # 그 거리가 최대 거리보다 작으면
    # cnt +=1 
    if (x <=x1 <=x+w) and (y<=y1 <= y+h):
        cnt += 1
        continue
    r = h/2
    d1 = ((x1-x)**2 + (y1-(y+r))**2)**(1/2)
    d2 = ((x1-(x+w))**2 + (y1-(y+r))**2)**(1/2)
    if d1 <= r or d2 <=r:
        cnt +=1
print(cnt)