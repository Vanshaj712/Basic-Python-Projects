def add():
    global x
    global y
    print(x + y)


def sub():
    global x
    global y
    print(x - y)


def prod():
    global x
    global y
    print(x * y)


def div():
    global x
    global y
    print(x / y)


def fldiv():
    global x
    global y
    print(x // y)


def sq():
    global x
    global y
    print(x ** y)

    print('''
        a - add
        s - subtract
        m - multiply
        d - divide
        fd - floor division
        sq - square       

        ''')


while True:
    print('''
        a - add
        s - subtract
        m - multiply
        d - divide
        fd - floor division
        sq - square       

        ''')
    x = int(input("Enter the first number: "))
    op = input("Enter  the operator: ")
    y = int(input("Enter the second number: "))

    if op == "a":
        add()

    elif op == "s":
        sub()
    elif op == "m":
        prod()

    elif op == "d":
        div()
    elif op == "fd":
        fldiv()

    elif op == "sq":
        sq()

    else:
        print("invalid  operater")


