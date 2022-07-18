a, b = map(int, input().split())
y = list(map(int, input().split()))
for i in range(a):
    if y[i] < b:
        print(y[i], end=" ")