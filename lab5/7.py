#Write a python program to convert snake case string to camel case string.

import re

def fun(s):
    word = s.split('_')
    c = word[0] + ''.join(word.capitalize() for word in word[1:])
    return c

with open(r'C:\Users\ASUS\Desktop\pp2\lab5\a.txt', 'r', encoding='utf-8') as file:
     g = file.read()

result = fun(g)
print(result)


