t = int(input())

for p in range(1,t+1):
    n = int(input())
    card = list(input().split())
    bin_1 = []
    bin_2 = []
    n_l = []
    cnt = 0
    if n%2 ==0:
        cnt = int(n/2)
        for i in range(cnt):
            bin_1.append(card[i])
        for j in range(cnt,n):
            bin_2.append(card[j])
        for k in range(len(bin_1)):
            n_l.append(bin_1[k])
            n_l.append(bin_2[k])
    else:
        cnt = int(n/2)+1
        for i in range(cnt):
            bin_1.append(card[i])
        for j in range(cnt,n):
            bin_2.append(card[j])
        for k in range(len(bin_2)):
            n_l.append(bin_1[k])
            n_l.append(bin_2[k])
        n_l.append(bin_1[cnt-1])
    
    print('#',end='')
    print(p,end=' ')
    print(*n_l)



