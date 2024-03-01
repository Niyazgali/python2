#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

# * - 0 or more occurences (or {0,})
# + - 1 or more occurences (or {1,})
# ? - 0 or 1 occurence (or {0,1})
# {2} - exactly 2 occurences
# {1,3} - from 1 occurence to 3 occurences
# {1,} - at least 1 occurence (same as +)
# {,3} - no more than 3 occurences

import re

with open(r'C:\Users\ASUS\Desktop\pp2\lab5\a.txt', 'r', encoding='utf-8') as file:
     g = file.read()

match = re.findall(r"ab*", g)
print(match)

