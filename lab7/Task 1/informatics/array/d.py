arr = input().split()
for i in range(1,len(arr)):
    if(int(arr[i]) > int(arr[i-1])):
        print(arr[i], end = ' ')