t = int(input())
per =  ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for i in range(1,t+1):
    n,k = map(int,input().split())
    li = []
    for j in range(n):
        mid,fin,res = map(int, input().split())
        total = (mid*0.35) + (fin*0.45)+(res*0.2)
        li.append(total)
    
    sco = li[k-1]

    li.sort(reverse=True)
    dig = n//10
    final = li.index(sco)//dig
    per_ = per[final]

    print(f'#{i} {per_}')
    
    
            
    