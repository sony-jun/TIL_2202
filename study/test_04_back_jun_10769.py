n = input()
sad = n.count(":-(")  # sad 개수
happy = n.count(":-)")  # happy 개수


if happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
