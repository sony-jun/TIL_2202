a, b = map(int, input().split())
y = [a, b]
for i in range(min(y), 0, -1):
    if a % i == 0 and b % i == 0:
        min_ = i
        break
max_ = a * b / min_
print(min_)
print(int(max_))
