for _ in range(3):
    li = []
    cnt = 1
    y = list(input())
    for i in range(7):
        if y[i] == y[i + 1]:
            cnt += 1
            li.append(cnt)
        else:
            cnt = 1
            li.append(cnt)
    print(max(li))
