a = []
b = []
for i in range(10):
    x = int(input())
    a.append(x)
for j in range(10):
    y = int(input())
    b.append(y)

a.sort()
b.sort()

print(sum(a[7:]),sum(b[7:]))



