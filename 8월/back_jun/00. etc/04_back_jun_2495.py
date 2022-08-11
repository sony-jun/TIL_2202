# 생각보다 어렵게 풀었음
for _ in range(3):
    y = list(input())
    li = []
    cnt = 1 #기본값이 0이 아닌 1
    for i in range(len(y)-1):
        
        if y[i] == y[i+1]:
            cnt += 1 
            li.append(cnt)
        elif y[i] != y[i+1]:
            cnt =1
            li.append(cnt)
        #실패
        #마지막 수가 빠지기 때문
        # cnt를 0이 아닌 1로 해결
    print(max(li))

