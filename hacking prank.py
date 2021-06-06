from time import sleep
import platform

print("to start hacking type s")
i = input("Do you wanna start the hacking: ")

def start():
    print(" hacking starting")
    sleep(2.0)

    print("20% hacked")
    sleep(2)

    print("40% hacked")
    sleep(2)

    print("60% hacked")
    sleep(2)

    print("80% hacked")
    sleep(2)

    print("100% hacked")
    sleep(2)

    print("your system is being hacked")

    print("here is your info:")
    sleep(1)

    print(platform.machine())
    print(platform.platform())
    print(platform.version())
    print(platform.uname())
    print(platform.system())
    print(platform.processor())


if i == "s":
    start()

else:
    pass

if __name__ == '__main__':
    start()
