a = int(input())
b = int(input())
c = int(input())
numbers = ['0',]
mul = str(a * b * c)
y = list(mul)
for i in range(10):
    print(y.count(str(i)))