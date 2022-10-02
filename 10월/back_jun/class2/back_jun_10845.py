import sys


t = int(sys.stdin.readline())
li = []
for _ in range(t):
    a = sys.stdin.readline().split()
    if a[0] == "push":
        li.append(a[1])
    elif a[0] == "pop":
        if len(li) == 0:
            print(-1)
        else:
            print(li.pop(0))
    elif a[0] == "size":
        print(len(li))
    elif a[0] == "empty":
        if len(li) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
    elif a[0] == "back":
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])
