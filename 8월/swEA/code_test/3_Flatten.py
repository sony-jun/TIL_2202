import sys

sys.stdin = open("_Flatten.txt")
for _ in range(1,11):
    n = int(input())
    number = list(map(int,input().split()))
    
   
    
    for i in range(n):
        max_ = max(number)
        min_ = min(number)
        j = number.index(max_)
        k = number.index(min_)
        number[j] -= 1
        number[k] += 1
               
        
        
    print(f'#{_} {max(number)-min(number)}')