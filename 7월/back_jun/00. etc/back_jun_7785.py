n = int(input())
dic = {}
name = []
for i in range(n):
    a,b = input().split()
    if b == 'enter':
        dic[a] = 'enter'
    else:
        if dic[a]:
            del dic[a]
for j in sorted(dic, reverse=True):
  print(j)
        

