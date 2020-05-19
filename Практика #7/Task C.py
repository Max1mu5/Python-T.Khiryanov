c = 0
sm = 0
tmp = int(input())
while tmp != 0:
    sm += tmp
    c += 1
    tmp = int(input())

print(round(sm / c, 2))