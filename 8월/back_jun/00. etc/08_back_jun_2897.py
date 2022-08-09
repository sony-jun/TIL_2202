from pprint import pprint 
n,m = map(int,input().split())
graph = []
dae0 = 0
dae1 = 0
dae2 = 0
dae3 = 0
dae4 = 0
truck = []
for _ in range(n):
    li = list(input())
    graph.append(li)
    
for i in range(n-1):
    for j in range(m-1):
        bin= []
        for k in range(2):
            for w in range(2):
                bin.append(graph[i+k][j+w])
        if '#' not in bin:
            truck.append(bin)
for q in truck:
        if q.count('X') == 0:
            dae0 += 1
        elif q.count('X') == 1:
            dae1 += 1
        elif q.count('X') == 2:
            dae2 += 1
        elif q.count('X') == 3:
            dae3 += 1
        elif q.count('X') == 4:
            dae4 +=1
        
print(dae0)
print(dae1)
print(dae2)
print(dae3)
print(dae4)

    