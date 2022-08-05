n = int(input())
for i in range(1,n+1):
    at, ap = map(int,input().split())
    at_num = list(map(int,input().split()))
    y = list(range(1,at+1))
    bin = []
    for j in range(len(y)):
        if y[j] not in at_num:
            bin.append(y[j])
    print(f'#{i}', end=' ')        
    print(*bin)
    


    






