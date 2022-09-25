for _ in range(1,11):
    a = input()
    queue = list(map(int,input().split()))

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

    print(f'#{_}',end=' ')
    print(*queue)
