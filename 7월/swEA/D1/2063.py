n = int(input())
y = map(int,input().split())
numbers = list(y)
numbers.sort()
len_value = n //2
print(numbers[len_value])