# words = list(map(int, input().split()))
# print(words)

# int로 받지말고 str로 받으면 해결

words = list(map(str, input().split()))
print(words)