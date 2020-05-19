arr = [int(input()) for i in range(3)]
arr.sort()

if arr[0] + arr[1] <= arr[2]:
    print('impossible')
elif arr[0]**2 + arr[1]**2 == arr[2]**2:
    print('right')
elif arr[0]**2 + arr[1]**2 < arr[2]**2:
    print('obtuse')
elif arr[0]**2 + arr[1]**2 > arr[2]**2:
    print('acute')
