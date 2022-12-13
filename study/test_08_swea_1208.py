for _ in range(1, 11):
    n = int(input())
    li = list(map(int, input().split()))
    for i in range(n):
        li[li.index(max(li))] -= 1
        li[li.index(min(li))] += 1
    cnt = (max(li)) - (min(li))
    print(f"#{_} {cnt}")
