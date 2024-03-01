import math
n=int(input())
s=int(input())
cot = 1 / math.tan(math.pi / n)
area = int(((1/4)*n*(s**2))*cot)
print(area)