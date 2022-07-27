# 딕셔너리가 편해보이긴 한데...일단 리스트로 접근 해봄

# 먼가 for문으로 안풀려서 다시 딕셔너리로...

n = input()
r = n.upper()
dic = {}
cnt = []
char = []
for i in r:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1
for j in dic.keys():
    cnt.append(dic[j])
for k in dic.keys():
    if  int(dic[k]) == int(max(cnt)):
        char.append(k)
  
if len(char) == 1:
    print(char[0])
else:
    print('?')

    
        





