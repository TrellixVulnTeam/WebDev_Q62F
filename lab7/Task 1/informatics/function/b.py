def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return a * power(a, n - 1)
 
a,b = map(str, input().split())
print(int(power(float(a),int(b))))