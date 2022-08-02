import sys
input = sys.stdin.readline

import heapq

n = int(input())
y = []
for _ in range(n):
    m = int(input())
    y.append(m)
heap = []


for i in y:
    if i != 0:
        heapq.heappush(heap,i)
        
        
        
    
    elif i == 0:
        
        if heap == []:
            print(0)
            
        else:
            if heap == []:
                print(0)
            else:
                print(heap[0])
                heapq.heappop(heap)
                
        
                

        
    
            
         

    
            
            

        


