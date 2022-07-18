# numbers = input().split()
# print(sum(numbers))

# 입력을 받으면 기본적으로 str로 받게 된다.
# 받을 때 자동으로 int로 받으면 문제 해결!
numbers = map(int,input().split())
print(sum(numbers))
