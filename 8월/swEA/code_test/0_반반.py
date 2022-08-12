t = int(input())

for _ in range(1,t+1):
    dic = {}
    bin_ = []
    n = list(input())
   
    for i in n:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
    if len(list(dic.values())) == len(list(dic.keys())) == 2:
        print(f'#{_} Yes')
    else:
        print(f'#{_} No')
