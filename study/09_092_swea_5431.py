t = int(input())
for _ in range(1, t + 1):
    a, b = map(int, input().split())
    li = list(map(int, input().split()))
    li_a = list(range(1, a + 1))
    li_new = []
    for i in range(a):
        if li_a[i] not in li:
            li_new.append(li_a[i])
    print(f"#{_}", end=" ")
    print(*li_new)

    """
    for num in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    stu = set(i for i in range(1, n + 1))
    stu_p = set(map(int, input().split()))

    print(f'#{num}', *stu - stu_p)
    """
