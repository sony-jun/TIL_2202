n = int(input())
numbers = map(int,input().split())
y = list(numbers)
mx = max(y)
cnt = []
for j in y:
    scam = j/mx *100
    cnt.append(scam)
print(sum(cnt)/n)




