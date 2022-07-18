# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# if 문에서 or을 쓸 때 조건이 잘못되었다
# 하나하나씩 전부 char==의 조건을 지정하자

word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char =="o"  or  char =="u":
        count += 1
    

print(count)