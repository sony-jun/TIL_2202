t = int(input())
dic = {}

cnt = 0
for i in range(t):
    a,b = map(int,input().split())
    if a in dic and dic[a] !=b:
            cnt +=1
    dic[a] = b

print(cnt)


    
    
    

        
           


    
