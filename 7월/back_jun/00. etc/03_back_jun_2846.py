n = int(input())
y = list(map(int, input().split()))
diff = 0
re = []
for i in range(1,n):
    if y[i-1] < y[i]:
        diff += y[i] - y[i-1]
    else:
        re.append(diff)
        diff = 0
re.append(diff)
print(max(re))
