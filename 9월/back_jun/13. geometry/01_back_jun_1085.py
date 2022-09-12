x,y,w,h = map(int,input().split())

li = []

li.append(x)
li.append(y)
li.append(w-x)
li.append(h-y)

print(min(li))