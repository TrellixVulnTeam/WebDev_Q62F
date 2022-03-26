import math
def is_perfect_square(i: int) -> bool:
    return math.isqrt(i) ** 2 == i
a=int(input())
b=int(input())
arr = []
for i in range(a,b+1):
    if(is_perfect_square(i)):
        arr.append(i)
print(*arr, sep=' ')