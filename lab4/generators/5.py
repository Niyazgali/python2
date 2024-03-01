def fun(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

down = fun(n)
for num in down:
    print(num)
