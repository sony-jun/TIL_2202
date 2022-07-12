sum = 0
i = 0
n = int(input())
while i <= n:
    sum = sum + i
    i += 1
print(sum)

print('==============================')
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)