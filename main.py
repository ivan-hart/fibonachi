MAX = int(input("enter the upper limit that you want to find "))

arr = [1,1]

print(arr[0])
while arr[1] < MAX:
    if arr[0] + arr[1] > MAX: break
    print(arr[1])
    a = arr[0]
    arr[0] = arr[1]
    arr[1] += a
print(arr[1])