t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    cnt = 0
    for i in range(a,b+1):
        zero = str(i)
        cnt += zero.count('0')
    print(cnt)
