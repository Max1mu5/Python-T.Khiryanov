N = int(input())
m = 0
k = 0
for i in range(N):
    t = int(input())
    if t == 1:
        k += 1
    else:
        k = 0
    if k > m:
        m = k
print(m)