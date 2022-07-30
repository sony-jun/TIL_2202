n = int(input())
cnt = 0
for i in range(n):
    char = list(input())
    
    n_c = []
    
    for j in range(len(char)-1):
        
        if char[j] != char[j+1]:
            n_c.append(char[j])
    n_c.append(char[-1])
    dic = {}
    for k in n_c:
        if k in dic:
            dic[k] += 1
        else:
            dic[k] = 1
    if max(dic.values()) == 1 :
        cnt += 1
        
print(cnt)



