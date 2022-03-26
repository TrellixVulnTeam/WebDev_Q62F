if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    z = set(arr)
    x = sorted(z)
    print(x[len(x)-2])
