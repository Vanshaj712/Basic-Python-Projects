import random
import pandas
pandas.Series
import pygame
args = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWZYZ!@#$%^&*'?/"

p_num = int(input("Enter the no. of password: "))

p_len = int(input("Enter the length of password: "))

for pa in range(p_num):

    password = ""
    for r in range(p_len):
        password += random.choice(args)

    print(password)