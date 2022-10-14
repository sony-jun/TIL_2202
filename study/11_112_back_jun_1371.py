import sys

input = sys.stdin.read

n = input()  # 입력을 받는다
li = []  # 빈 리스트
dic = {}  # 알파벳 카운트를 위한 빈 딕셔너리
for i in n:
    if i != " " and i != "\n":  # 입력받은 값중에 띄어쓰기와 줄바꾸는엔터를 제외하고
        li.append(i)  # 빈 리스트에 전부 보내면, 띄어쓰기와 줄바꾸기는 없는채로 리스트가 채워진다
for j in li:
    if j in dic:
        dic[j] += 1
    else:
        dic[j] = 1  # 알파벳에 대한 카운트를 딕셔너리로 완성하게 된다
max_ = max(dic.values())  # 벨류값(숫자)가 가장 큰 수를 max_로 지정한다
choi_bin = []  # 새로운 빈 리스트
for key, value in dic.items():
    if value == max_:  # 벨류값이 가장 큰 수 max와 같을 경우
        choi_bin.append(key)  # 빈리스트로 값을 보내준다
choi_bin.sort()  # 알파벳 순으로 정렬하게하기 위해서 정렬을 사용한다.
for k in choi_bin:
    print(k, end="")  # 띄어쓰기 없이 출력한다.

"""
import sys

input = sys.stdin.read

alpha = [0] * 26
sentence = input().replace("\n", "").replace(" ", "")

for s in sentence:
    if s.isalpha():
        alpha[ord(s) - 97] += 1
mx = max(alpha)

for i in range(26):
    if mx == alpha[i]:
        print(chr(i + 97), end="")
"""
