n = int(input())
dic = {}
card =  []
for i in range(n):
    m = int(input())
    if m in dic:
        dic[m] += 1
    else:
        dic[m] = 1

    if i == 0:
        temp = m
    if dic[temp] == dic[m]:
        temp = min(temp, m)
    elif dic[temp] < dic[m]:
        temp = m
print(temp)
