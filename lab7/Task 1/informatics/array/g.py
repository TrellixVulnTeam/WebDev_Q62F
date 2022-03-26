arr = input().split()
ind = 0
for i in range(0,len(arr)):
    if(int(arr[i]) > int(arr[ind])):
        ind = i
        
print(arr[ind], ind)