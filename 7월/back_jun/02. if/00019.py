a, b = map(int,(input().split()))

     
if a >0 and b < 45:
    a += -1
    b += 15
elif a == 0 and b < 45:
    a += 23
    b += 15
elif a == 0  and b > 45:
    b += - 45
else:
    b += -45
print(a,b)