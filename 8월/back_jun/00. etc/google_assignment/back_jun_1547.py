list_ = [1,2,3]

n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    list_[a-1], list_[b-1] = list_[b-1],list_[a-1]
print(list_.index(1)+1)