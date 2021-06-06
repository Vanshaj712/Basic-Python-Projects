import random
dice = [1,2,3,4,5,6]

def one():
    print("*")

def two():
    print("*    *")


def three():
    print("*   *   *")

def four():
    print("*     *")
    print("*     *")

def five():
    print("*      *")
    print("    *   ")
    print("*      *")

def six():
    print("*   *   *")
    print("*   *   *")


ch = random.choice(dice)

if ch == 1:
    one()

elif ch == 2:
    two()

elif ch == 3:
    three()

elif ch == 4:
    four()

elif ch == 5:
    five()

else:
    six()






