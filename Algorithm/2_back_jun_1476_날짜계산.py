# 성공!

e, s, m = map(int, input().split())  # 지구 태양 달의 정수값을 받으므로
cnt = 1
# 각각의 최소공배수 혹은 바이오 리듬을 생각하면 비교적 간단하게 알 수 있다
while True:
    if (
        (cnt - e) % 15 == 0 and (cnt - s) % 28 == 0 and (cnt - m) % 19 == 0
    ):  # 모든 값의 나머지가 0일때 년도를 알 수 있게 된다!
        break
    cnt += 1
print(cnt)
