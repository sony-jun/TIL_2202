for _ in range(1, 11):  # 개수가 10개로 제한 되어 있으니까 범위를 10개로 맞춰줌, 1,11인 이유는 밑에 프린트 할때 편하라고
    number = int(input())  # 길이를 입력 받음
    gualho = list(input())  # 괄호(문자)를 입력받음

    li_1 = []
    li_2 = []
    li_3 = []
    li_4 = []
    cnt = True  # 하나의 리스트로 하려했으나 실패해서 리스트를 각각으로 만들면 되지 않을까 해서 4개로 쪼갬, T/F는 T를 기본으로 설정

    for i in range(number):
        if gualho[i] == "(":  # 여는 괄호를 받으면
            li_1.append(gualho[i])  # 여는 괄호를 리스트 1에 추가
        if gualho[i] == ")":  # 닫는 괄호를 받으면
            if len(li_1) >= 1:  # 리스트가 남아 있을 경우
                li_1.pop()  # 들어있는 여는 괄호 '('를 빼 준다
            else:  # 리스트가 빈 리스트일 경우
                cnt = False  # 값을 False로 바꿔준 후
                break  # 어차피 닫는 괄호로 시작하면 무조건 틀리기 때문에 break해준다
    for i in range(number):
        if gualho[i] == "{":
            li_2.append(gualho[i])
        if gualho[i] == "}":
            if len(li_2) >= 1:
                li_2.pop()
            else:
                cnt = False
                break
    for i in range(number):
        if gualho[i] == "[":
            li_3.append(gualho[i])
        if gualho[i] == "]":
            if len(li_3) >= 1:
                li_3.pop()
            else:
                cnt = False
                break
    for i in range(number):
        if gualho[i] == "<":
            li_4.append(gualho[i])
        if gualho[i] == ">":
            if len(li_4) >= 1:
                li_4.pop()
            else:
                cnt = False
                break  # 각각의 괄호에 대해서 똑같은 방법으로 구해준다

    if (
        len(li_1) + len(li_2) + len(li_3) + len(li_4)
    ) > 0:  # 입력받은 괄호에 대해서 여는 괄호가 남아있을 경우
        cnt = False  # 표시를 false로 바꿔준다
    if cnt == True:  # 이거 기본이 트루가1이고 펄스가0일껀데 어떻게 표시하는지 까먹어서 if문을 한번 더 사용함
        t = 1
    else:
        t = 0
    print(f"#{_} {t}")  # 값 표시


"""
for test_case in range(1, 11):
    n = int(input())
    bracket = input()
    stack = []
    left = ["<", "{", "[", "("]
    right = [">", "}", "]", ")"]
    answer = 1
    for i in bracket:
        if i in left:
            stack.append(i)
        else:
            if left.index(stack[-1]) == right.index(i):
                stack.pop()
            else:
                answer = 0
                break
    print(f"#{test_case} {answer}")
"""
