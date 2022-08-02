# 인풋을 숫자 2개 받고
# EX) 4개 , 2개의 더미
# 첫번째 더미2개
# 3,1
# 두번째 더미 2개
# 4,2

# 1부터 n까지의 수열이 존재한다고 할때
# 끝에서 부터 하나씩 순서대로 뽑아올 수 있다면 YES
# 1,3,2처럼 순서대로 뽑아오지 못한다면 NO
# 받을수 있는 더미? 2*M의 더미의 정보
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

list_2 = []
for i in range(m): #처음에 m값이 2m으로 넣어봤는데 바로 2배가 되길래  m으로 수정
    a = int(input())
    list_number = list(map(int,input().split()))
    for j in range(0,len(list_number)-1):
        if list_number[j] < list_number[j+1]:# 조건식을 반대로 하고 else문에 넣었었는데 다시 고치면서 해보니
            list_2.append(list_number[j+1]) # 그렇게 하는것보다 이렇게만 하면 되는걸 발견하고 고침
        
            
if list_2 == []:
    print('Yes')
else:
    print('No')
    







