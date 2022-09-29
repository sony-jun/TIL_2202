t = int(input())
for _ in range(t):
    li = input().split()
    for i in li:
        print(i[::-1], end=" ")
