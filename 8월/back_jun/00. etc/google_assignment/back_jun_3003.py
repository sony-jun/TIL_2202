li = [1,1,2,2,2,8]

y = list(map(int,input().split()))
for i in range(len(li)):
    print((li[i]-y[i]),end=' ')