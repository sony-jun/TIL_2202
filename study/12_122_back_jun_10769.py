a = input()
sad = a.count(":-(")
happy = a.count(":-)")
if sad == happy == 0:
    print("none")
else:
    if sad > happy:
        print("sad")
    elif sad < happy:
        print("happy")
    else:
        print("unsure")
