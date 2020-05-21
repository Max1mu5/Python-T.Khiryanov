N = int(input())

def fibonacci(x):
    if x in [1, 2]:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

print(fibonacci(N))

# 1 1 2 3 5 8 13