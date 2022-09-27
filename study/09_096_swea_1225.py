for _ in range(1, 11):
    a = input()
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

    print(f"#{_}", end=" ")
    print(*queue)


"""
from collections import deque

for _ in range(10):
    n = int(input())
    nums = deque(list(map(int, input().split())))
    cnt = 1
    while True:
        if cnt == 6:
            cnt = 1
        nums[0] -= cnt
        if nums[0] <= 0:
            nums[0] = 0
            nums.rotate(-1)
            break
        else:
            cnt += 1
            nums.rotate(-1)
    print(f"#{n}", end=" ")
    print(*nums, sep=" ")
"""
