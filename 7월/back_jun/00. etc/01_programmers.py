def solution(absolutes, signs):
    answer = 0
    for i in range(0,3):
        if signs[i] == True:
            answer += int(absolutes[i])
        else:
            answer -= int(absolutes[i])
    return answer