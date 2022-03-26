a=int(input())
b=int(input())
c=int(input())
d=int(input())
arr = []
for i in range(a,b+1):
    if(i % d == c):
        arr.append(i)
print(*arr, sep=' ')