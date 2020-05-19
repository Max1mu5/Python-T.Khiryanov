arr = [0] * 100
N = int(input())
for i in range(N):
    arr[int(input())] += 1

index = -1
mx = 0
for i in range(100):
    if arr[i] > mx:
        mx = arr[i]
        index = i

print(index)