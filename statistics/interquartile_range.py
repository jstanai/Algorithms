#interquartile range
n = input()
a = list(map(int, input().split(' ')))
f = list(map(int, input().split(' ')))

def iqr(a, f, n):

    pairs = []
    for i in range(a):
        pairs.append({f[i]: a[i]})

    pairs = sorted(pairs, key = )