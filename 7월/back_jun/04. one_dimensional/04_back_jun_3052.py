nums = [int(input()) for i in range(10)]
cnt = []

for j in nums:
    n = j%42
    cnt.append(n)
m = set(cnt)
print(len(m))