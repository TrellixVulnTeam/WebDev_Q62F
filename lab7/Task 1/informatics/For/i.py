a=int(input())
cnt=2
i=2
while(i<a):
    if(a % i == 0):
        cnt += 1
    i += 1
print(cnt)