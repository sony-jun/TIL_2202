import sys
input = sys.stdin.read


n = int(input())

li = []
for i in range(44444444):
    if '0' not in str(i) and '1' not in str(i) and '2' not in str(i) and '3' not in str(i) and '5' not in str(i) and '6' not in str(i) and '8' not in str(i) and '9' not in str(i):
        li.append(i)
cnt = 0
for j in range(len(li)):
    if li[j] > n:
        cnt = li[j-1]
        break
print(cnt)




