#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

with open(r'C:\Users\ASUS\Desktop\pp2\lab5\a.txt', 'r', encoding='utf-8') as file:
     g = file.read()

seq = re.findall(r"\b[А-Я][а-я]+", g)
print(seq)