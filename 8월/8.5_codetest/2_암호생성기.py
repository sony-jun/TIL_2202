n = 10
for t in range(1, n+1):
    tc = int(input())
    queue = list(map(int, input().split()))

    i = 1
    while True:
        if i > 5:
            i = 1
        m = queue.pop(0) - i
        if m <= 0:
            queue.append(0)
            break
        queue.append(m)
        i += 1
    print(f'#{t}', end=' ')
    print(*queue)
