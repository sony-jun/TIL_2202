import sys
input = sys.stdin.read

# english is a west germanic
# language originating in england
# and is the first language for
# most people in the united
# kingdom the united states
# canada australia new zealand
# ireland and the anglophone
# caribbean it is used
# extensively as a second
n = input() # abca
li = []
dic = {}
for i in n:
    if i != ' ' and i != '\n':
        li.append(i) # 띄어쓰기, 엔터가 아닌 알파벳만 들어감
for j in li: 
    if j in dic:
        dic[j] += 1 # a, b,c, a
    else:
        dic[j] = 1
max_ = max(dic.values()) #2
choi_bin = [] #a
for key,value in dic.items(): #items() = key(),value()
    if value == max_: #2
        choi_bin.append(key)
choi_bin.sort() # c b -> [b, c]
for k in choi_bin:
    print(k,end='') #cb





