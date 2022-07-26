n = 5
sum_= []
for i in range(1,n+1):
    numbers = map(int,input().split())
    y = sum(list(numbers))
    sum_.append(y)
max_ = max(sum_)
print((sum_.index(max_)+1),max_)

