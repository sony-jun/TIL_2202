# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)

# pprint의 위치가 for문안에 포함돼 있지 않게 되면
# 마지막에 들어간 Salal berry만 들어가게 된다.
# for문 안에 pprint위치를 넣어주면 다 들어가게 됨


from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1
    pprint(fruit_count)