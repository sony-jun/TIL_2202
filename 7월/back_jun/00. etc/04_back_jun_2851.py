cnt = []
m = 0
mum = []
for i in range(10):
    
    n = int(input())
    cnt.append(n)
for j in range(len(cnt)):
    m += cnt[j]
    mum.append(m) 
    if m >= 100:
         
        break
if len(mum) == 1:
    print(mum[0])
else:
    if abs(100-mum[-1]) <= (100-mum[-2]):
        print(mum[-1])
    else:
        print(mum[-2])    


    


