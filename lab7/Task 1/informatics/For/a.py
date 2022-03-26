a = int(input())
b = int(input())
arr = []
for i in range(a,b+1):
    if(i % 2 == 0):
        arr.append(i)
print(*arr, sep = ' ')