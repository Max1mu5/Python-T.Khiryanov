a = int(input())
b = int(input())

while a != b:
    if b > a:
        b -= a
    else:
        a -= b

print(a)