a,b = map(int,input().split())

li = list(map(int,input().split()))

so = sorted(li,reverse=-1)

print(so[b-1])
