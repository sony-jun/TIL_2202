# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

# 2answer.append(number * 2)
# AttributeError: 'dict' object has no attribute 'append'
# 라고 나온다
# 2번째 anwer을 []로 받으면 해결

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)