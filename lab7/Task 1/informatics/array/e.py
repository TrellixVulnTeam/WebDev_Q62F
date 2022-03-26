arr = input().split()
for i in range(1,len(arr)):
    if(int(arr[i]) > 0 and int(arr[i-1]) > 0):
        print(arr[i-1], arr[i], end = ' ')
        break
    if(int(arr[i]) < 0 and int(arr[i-1]) < 0):
        print(arr[i-1], arr[i], end = ' ')
        break    