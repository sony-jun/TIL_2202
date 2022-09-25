t = int(input())

li = []

for i in range(2667000):
    six = str(i)
    if '666' in six:
        li.append(six)
        if len(li) == t:
            break
print(li[t-1])
