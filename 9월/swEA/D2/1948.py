t=int(input())
date=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(1,t+1):
    print(f'#{i}',end=' ')
    m,d1,n,d2=map(int,input().split())
    sum=1
    for x in range(n-1):
        sum+=date[x]
    sum+=d2
    sum-=d1
    for x in range(m-1):
        sum-=date[x]
    print(sum)