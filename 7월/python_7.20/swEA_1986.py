n = int(input())
for i in range(n):
    cnt = 0
    x = int(input())
    for m in range(0,x+1):
        if m % 2 == 0:
            cnt += -m
        else:
            cnt += m
    print(f'#{i+1} {cnt}')

    