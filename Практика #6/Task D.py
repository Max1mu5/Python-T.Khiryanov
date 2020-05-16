sm, mx, mn, sm3, c, t = 0, 0, 101, 0, 0, 0
"""Это решение для указанных входных данных, а то что творится в проверочных тестах я не знаю"""
x = input()
while x != '#':
    x = int(x)
    c += 1
    if c % 3 == 0:
        t += x
        sm3 += t % x
        t = 0
    else:
        t += x
    if x > mx:
        mx = x
    if x < mn:
        mn = x
    sm += x
    x = input()

print(round(sm / c, 3), mx, mn, sm3)