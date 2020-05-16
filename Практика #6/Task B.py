x = input().split()
y = 0
c = 0
if x[0] == '0':
    t = input()
    y = -1

if y != -1:
    y = x[2]

a = int(x[0])
while a < int(y):
    c += 1
    a *= (1 + int(x[1])/100)
    a = int(a * 100) / 100

print(c)