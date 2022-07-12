a, b, c = input().split()
a = int(a)  
b = int(b)
c = int(c)
min = a
numbers = [a, b, c]
for i in numbers:
    if min > i:
        min = i
print(min)