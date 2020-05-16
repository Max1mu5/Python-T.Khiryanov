s = input()
k = int(input())
if k > 0:
    print(s * k)
elif k < 0:
    c = 0
    for _ in s:
        c += 1
    if c % (-k) == 0 and (-k) != c:
        for i in range(c // (-k)):
            print(s[i], end='')
    else:
        print('NO SOLUTION')