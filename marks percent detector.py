import psycopg2


def per():
    global x
    global y

    return x / y * 100

while True:
    sub = input("Enter the subject name: ")

    x = float(input("enter the obtained marks: "))

    y = int(input("Enter the total marks: "))



    print("Your percentage in", sub ,"is",per())
