# Quartile Computation
n = int(input())
arr = list(map(int, input().split(' ')))

# Alternative: Use UDF median
from statistics import median

def quartiles(arr):

    arr = sorted(arr)
    q2 = statistics.median(arr)

    val = arr[n//2]
    if val == q2:
        lh_upper = n//2 - 1
        uh_lower = n//2 + 1
    else: 
        lh_upper = n//2 - 1
        uh_lower = n//2

    lh = arr[0:lh_upper + 1]
    uh = arr[uh_lower:]

    q1 = median(lh)
    q3 = median(uh)

    return q1, q2, q3

q1, q2, q3 = quartiles(arr)
print(int(q1))
print(int(q2))
print(int(q3))