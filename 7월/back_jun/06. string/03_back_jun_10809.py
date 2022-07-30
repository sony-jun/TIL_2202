n = input()
cnt = []
alpa = 'abcdefghijklmnopqrstuvwxyz'
for i in alpa:
    if i in n:
        print(n.index(i), end=' ')
    else:
        print(-1, end = ' ')
