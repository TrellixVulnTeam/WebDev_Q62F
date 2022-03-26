arr = input().split()
cnt = 0
for i in range(0,len(arr)):
    if(int(arr[i]) >0):
        cnt += 1
print(cnt)