x = int(input())
y = input()
y = list(y)
y = list(map(int,y))
y.reverse()
mud = int(y)
for i in y:
    n = x * i
    print(n)
print(x*mud)