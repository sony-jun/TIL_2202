n = input()

answer = n
numbers = {'zero':0,'one':1,'two':2,'three':3,
              'four':4,'five':5,'six':6,'seven':7,
              'eight':8,'nine':9}

for i in numbers.keys():
    if i in n:
        answer = answer.replace(i,str(numbers[i]))
print(int(answer))
# def solution(s):

#     num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for i, j in enumerate(num_list):
#         s = str(i).join(s.split(j))
#     return int(s)