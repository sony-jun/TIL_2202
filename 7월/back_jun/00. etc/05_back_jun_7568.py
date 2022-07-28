n = int(input())
xy = []


for i in range(n):
    xy.append(list(map(int,input().split())))
    
    
    
for j in range(n):
    rank = 1
    for k in range(n):
        if j != k:
            if (xy[j][0] < xy[k][0]) and (xy[j][1] < xy[k][1]):
                rank +=1
    print(rank,end = ' ') 
    
    

    


