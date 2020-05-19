N = int(input())

fence = []
for i in range(N):
    tmp = []
    for j in range(3):
        tmp.append(int(input()))
    fence.append(tmp)

M = int(input())
wood_numbers = []
for i in range(M):
    wood_numbers.append(int(input()))

ans = [0] * M
top = 0
for wood in wood_numbers:
    for interval in fence:
        if interval[0] < wood < interval[1]:
            ans[top] = interval[2]
    top += 1

print(*ans)
