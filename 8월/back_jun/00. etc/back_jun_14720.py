n = int(input())
cnt = 0
number = list(map(int,input().split()))
for j in range(n):
    if number[j] == cnt %3:
        cnt += 1
print(cnt)
