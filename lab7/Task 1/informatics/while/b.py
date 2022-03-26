a = int(input())
b = 2
while(b != a):
    if(a % b == 0):
        print(b)
        exit(0)
    b += 1
print(b)