import sys
from collections import Counter
# 내장 함수인 counter를 이용해서 풀이
N = int(sys.stdin.readline())
num = list()
for x in range (N) :
    temp = int(sys.stdin.readline())
    num.append(temp)

num.sort()
mean = round(sum(num) / N)
median = num[int(N / 2)]

mode = Counter(num).most_common()
mode_value = 0

if len(mode) == 1:
    mode_value = mode[0][0]
elif mode[0][1] == mode[1][1]:
    mode_value = mode[1][0]
else:
    mode_value = mode[0][0]

range_N = num[-1] - num[0]

print(mean)
print(median)
print(mode_value)
print(range_N)

