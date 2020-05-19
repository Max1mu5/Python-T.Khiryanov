arr = [0]*6
arr[0] = int(input())
mx = arr[0]
for i in range(1, 6):
    arr[i] = int(input())

while arr[5] != 0:
    if arr[0] > mx:
        mx = arr[0]
    for i in range(5):
        arr[i] = arr[i + 1]
    arr[5] = int(input())

print(mx)