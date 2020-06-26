cars = ["Nissan", "Ford"]


def myFunction(name):
    lst = []
    for i in cars:
        msg = "{}'s car is a {}.".format(name, i)
        lst.append(msg)
    return lst


def userName():
    x = True
    while x:
        name = input("What's your name? ")
        if name == "":
            print("Please enter your name.")
        else:
            x = False
    lst = myFunction(name)
    for i in lst:
        if name == "Scott":
            y = slice(1)
            print("{}'s car is a {}.".format(name.capitalize(), cars[0]))
            break
        elif name == "Amber":
            z = slice(2)
            print("{}'s car is a {}.".format(name.capitalize(), cars[1]))
            break
        elif name != "Scott" or "Amber":
            print("Please only submit members of your household. Thank you!")
            return userName()
        else:
            return


userName()
