def fun(n):
    for i in range(1, n+1):
        yield i**2


n = int(input())
squares = fun(n)
for num in squares:
    print(num)
