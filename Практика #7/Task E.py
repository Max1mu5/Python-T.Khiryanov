N = int(input())
arr = [0, 0, 1]
c = 0

while arr[2] <= N:
    tmp = arr[2]
    arr[2] = arr[0] + arr[1] + arr[2]
    arr[0] = arr[1]
    arr[1] = tmp

    c += 1

print(c + 2)
