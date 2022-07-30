

n = int(input())
for i in range(n):
    length = (map(int,input().split()))
    dic = {}
    for j in length:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1
    for k in dic:
        if dic[k] == 3:
            print(f'#{i+1} {k}')
        if dic[k] == 1:
            print(f'#{i+1} {k}')



