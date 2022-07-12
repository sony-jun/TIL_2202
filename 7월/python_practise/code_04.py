mul = 1
i = 1
n = int(input())
while i <= n:
    mul = mul * i
    i += 1
print(mul)

print('==============================')
mul = 1
for i in range(1, n + 1):
    mul *= i
print(mul)