n = int(input())
t = int(input())
cnt = 0
for _ in range(t):
    a, b = map(int, input().split())
    c = a * b
    cnt += c

if n == cnt:
    print("Yes")
else:
    print("No")
