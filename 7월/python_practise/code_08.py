numbers = [0, 20, 100, 50, -60, 50, 100]
max = numbers[0]
second = numbers[0]
for i in numbers:
    if max < i:
         max = i
numbers = list(set(numbers))    
numbers.remove(max)
for i in numbers:
    if second < i:
        second = i
print(second)