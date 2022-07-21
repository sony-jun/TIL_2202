n = int(input())
for i in range(1, n+1):
    T,M,t,m = map(int,input().split())
    f = T + t
    s = M + m
    if f > 12 and s > 60:
        f = f - 11
        s = s - 60
    elif f > 12 :
        f = f - 12
    elif s > 60:
        s = s - 60
        f = f + 1 
    print (f'#{i} {f} {s}')
