t = int(input())

for _ in range(1,t+1):
    n = input()
    y =n.replace('a',"")
    b = y.replace('e',"")
    j = b.replace('i',"")
    k =j.replace('o',"")
    r = k.replace('u',"")
    print(f'#{_} {r}')
