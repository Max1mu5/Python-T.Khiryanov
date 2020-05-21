import sys

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


print(fac(998))                # Максимальная глубина рекурсии - 998
print(sys.getrecursionlimit()) # Максимальная глубина стека вызова - 1000
