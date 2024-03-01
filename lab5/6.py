#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

with open(r'C:\Users\ASUS\Desktop\pp2\lab5\a.txt', 'r', encoding='utf-8') as file:
     g = file.read()

replace = re.sub(r"[ ,.]", ":", g) 
print(replace)