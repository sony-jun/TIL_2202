n = int(input())
for i in range(n):
    numbers = map(int,input().split())
    y = list(numbers)
    m = sorted(y)
    m.pop(0)
    m.pop(-1)
    avg = float(sum(m)/(len(y)-2))
    print(f'#{i+1} {round(avg)}')