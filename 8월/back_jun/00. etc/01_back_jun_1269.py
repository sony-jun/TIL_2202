a,b = map(int,input().split())

x = set(map(int,input().split()))
y = set(map(int,input().split()))

print(len(x-y)+len(y-x))