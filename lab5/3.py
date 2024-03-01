#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

with open(r'C:\Users\ASUS\Desktop\pp2\lab5\a.txt', 'r', encoding='utf-8') as file:
     g = file.read()

seq = re.findall(r"\w[а-я]+_\w[а-я]+", g)
print(seq)

