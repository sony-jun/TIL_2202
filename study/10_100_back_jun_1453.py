N = int(input())
li = list(map(int,input().split()))
bin_ = len(list(set(li)))
print(len(li)-bin_)