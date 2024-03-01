#Write a Python program to insert spaces between words starting with capital letters.

import re

with open(r'C:\Users\ASUS\Desktop\pp2\lab5\a.txt', 'r', encoding='utf-8') as file:
     g = file.read()

insertie = re.sub(r'[А-Я]',' \1',g)

print(insertie)