# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# for문에서 count가 빠져나와 있는것을 볼 수 있다
# for 문에서 벗어나지 않게 바로 위 total과 줄을 맞춰준다


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)