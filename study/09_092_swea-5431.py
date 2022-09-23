t = int(input())
for _ in range(1,t+1):
    a,b = map(int, input().split())
    li = list(map(int, input().split()))
    li_a = list(range(1,a+1))
    li_new = []
    for i in range(a):
        if li_a[i] not in li:
            li_new.append(li_a[i])
    print(f'#{_}', end=' ')
    print(*li_new)