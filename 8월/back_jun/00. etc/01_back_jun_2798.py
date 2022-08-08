a,b = map(int,input().split())
numbers = list(map(int,input().split()))
cnt = 0
for i in range(a-2):
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            mum = numbers[i] + numbers[j] + numbers[k]
            if cnt<mum <=b:
                cnt =mum
            if mum ==b:
                break
print(cnt)



