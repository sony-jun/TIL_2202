# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    i = 0
    
    for i in range(i, len(numbers)):
        for j in range(i+1,len(numbers)):
            answer += [int(numbers[i])+int(numbers[j])]

        
    answer = set(answer)
    answer = sorted(list(answer))    
    
    return answer
    


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
