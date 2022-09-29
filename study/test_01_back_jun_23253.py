import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
for i in range(m):
    k1 = int(input())
    k2 = list(map(int, input().split()))
    for j in range(k1 - 1):
        if k2[j] < k2[j + 1]:
            cnt += 1
            print("No")
            break
if cnt == 0:
    print("Yes")
