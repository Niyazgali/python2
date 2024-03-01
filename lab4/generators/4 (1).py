def fun(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input())
b = int(input())
squares = fun(a, b)
for num in squares:
    print(num, end=", ")
