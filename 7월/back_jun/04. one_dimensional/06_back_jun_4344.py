n = int(input())
for i in range(1,n+1):
    cnt = []
    numbers = map(int,input().split())
    y = list(numbers)
    m = y[0]
    del y[0]
    avg = float(sum(y)/m)
    
    for j in y:
        if j > avg:
            cnt.append(j)
    per = float(len(cnt)/len(y)*100)
    print('%.3f' %per + '%')

