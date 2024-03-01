def fun(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input())
eN = fun(n)
print(*eN, sep=", ")
