from sys import exit
n= int(input())
k = int(input())
if ((n!=1 and k!=1) or (n==1 and k==1)):
    print("YES")
    exit(0)
print("NO")