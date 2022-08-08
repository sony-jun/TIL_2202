# word = list(input())
# char = list(input())
# cnt = 0
# li = []
# for i in range(len(word)):
#     for j in range(len(word)):
#         if word[i:j] == char:
#             li.append(list(range(i,j)))

# print(li)
# nul = li
# for k in range(len(li)-1):
#     for w in range(len(li)-1):
#         if li[k][w] == li[k+1][w+1]:
#             del nul[k+1][w+1]
# print(nul)
# li안에 있는 값안에 겹치는 값이 있다면 
# 그 값을 제거하고 카운트 하려고 했는데 구현을 못했다...
n = input()
c = input()
print(n.count(c)) 



