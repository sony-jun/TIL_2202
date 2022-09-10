import sys
input = sys.stdin.readline

a, b = map(int, input().split())
li_1 = []
dic = {}
for i in range(a):
    pk = input().rstrip()
    li_1.append(pk)
    dic[pk] = i +1

for j in range(b):
    query = input().rstrip()

    if query.isdigit():
        print(li_1[int(query)-1])
    else:
        print(dic[query])




