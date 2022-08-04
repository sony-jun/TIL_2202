matrix = []
for i in range(4):
    i,j,x,y = map(int,input().split())
        

    for a in range(i,x):
        for b in range(j,y):
            matrix.append([a,b])

new_list = []

for v in matrix:
    if v not in new_list:
        new_list.append(v)
        
print(len(new_list))
    
