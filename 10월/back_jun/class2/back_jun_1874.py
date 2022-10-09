n = int(input())

count = 1
stack = []
result = []

for _ in range(n):
    data = int(input())

    while count <= data:
        stack.append(count)
        result.append("+")
        count += 1

    if stack.pop() == data:
        result.append("-")

    else:
        print("NO")
        exit(0)

print("\n".join(result))
