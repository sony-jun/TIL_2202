
n = int(input())

for i in range(n):
    dic = {}
    cnt_list = []
    case_number = int(input())
    number = list(map(int,input().split()))
    for j in number:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1
    y = max(dic.values())
    for k in dic:
        if dic[k] == int(y):
            cnt_list.append(k)
    cnt_list.sort(reverse=True)
    print(f'#{case_number} {cnt_list[0]}')



