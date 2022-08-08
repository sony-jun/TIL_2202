t = int(input())
for _ in range(t):
    grade = list(map(int,input().split()))
    li = []

    # 둘째 줄에는 가장 높은 점수, 낮은 점수, 성적을 내림차순으로 
    # 정렬했을 때 가장 큰 인접한 점수 차이를 
    # 예제 출력과 같은 형식으로 출력한다.
    max_ = max(grade[1:])
    min_ = min(grade[1:])
    y = sorted(grade[1:])
    for i in range(0,len(y)-1):
        gap = abs(y[i]-y[i+1])

        li.append(gap)

    print(f'Class {_+1}')
    print(f'Max {max_}, Min {min_}, Largest gap {(max(li))}')



#Class 1
#Max 78, Min 23, Largest gap 46
#Class 2
#Max 99, Min 25, Largest gap 25

    
