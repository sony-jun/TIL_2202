n = int(input())
for i in range(n):
    s = input()
    y = list(s)
    m = list(reversed(y))
    if y == m:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')
 