for t in range(1, 11):
    n = int(input())
    li = list(input())
    cnt = []
    y = True
    op = ["(", "[", "{", "<"]
    cl = [")", "]", "}", ">"]
    for i in range(n):
        if li[i] in op:
            cnt.append(li[i])
        if li[i] in cl:

            if cl.index(li[i]) == op.index(cnt[-1]):
                cnt.pop()
            else:
                break

    if len(cnt) > 0:
        y = False

    if y == True:
        m = 1
    else:
        m = 0

    print(f"#{t} {m}")
