from collections import Counter
if __name__ == '__main__':
    z = {}
    mini=100000
    for _ in range(int(input())):
        name = input()
        score = float(input())
        z[name] = score
        if(score < mini): mini = score
    secondmini=0
    for key in sorted(z.keys(), key = z.get):
        if(z[key] != mini):
            secondmini=z[key]
            break
    counter = Counter(sorted(z))
    for key in sorted(counter.keys(), key = counter.get, reverse=True):
        if(z[key] == secondmini):
            print(key)
