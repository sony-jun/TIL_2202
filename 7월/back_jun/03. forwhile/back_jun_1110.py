n = int(input())
cnt = 0
number = n

while True:
    a = number // 10
    b = number % 10
    c = (a + b) % 10
    number = (b * 10) + c
    cnt +=1
    
    if (number == n):
        break
print(cnt)