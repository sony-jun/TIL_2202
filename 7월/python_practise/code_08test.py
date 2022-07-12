numbers = [0, 20, 100, 50 ]
max = numbers[0]
second = numbers[0]
for i in numbers:
    if max < i:
         second = max
         max = i
print(second)