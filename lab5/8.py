#Write a Python program to split a string at uppercase letters.

import re

with open(r'C:\Users\ASUS\Desktop\pp2\lab5\a.txt', 'r', encoding='utf-8') as file:
     g = file.read()

def fun(match):
     return match.group(0).upper()

splitie = re.sub(r'[а-я]', fun, g)

print(splitie)