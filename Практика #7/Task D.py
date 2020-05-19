mx = 0
tmp = int(input())
while tmp != 0:
    if tmp > mx and tmp % 2 == 0:
        mx = tmp
    tmp = int(input())

print(mx)