a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_cnt = 0
b_cnt = 0
for i in range(10):
    if a[i]>b[i]:
        a_cnt +=3
    elif a[i]<b[i]:
        b_cnt +=3
    else:
        a_cnt+=1
        b_cnt+=1
print(a_cnt,b_cnt)
if a_cnt>b_cnt:
    print('A')
elif a_cnt<b_cnt:
    print('B')
elif a_cnt == b_cnt:
    for j in range(9,0,-1):
        if a == b:
            print('D')
            break
        elif a[j]<b[j]:
            print('B')
            break
        elif a[j]>b[j]:
            print('A')
            
