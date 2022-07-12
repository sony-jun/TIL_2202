n = int(input())
sum = 0
a = 0
for i in range(1, n+1) :
  sum += i
  a += 1
  if sum >= n :
    break 
print(a)