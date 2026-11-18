def _sort(arr):
    res = [x for x in arr]
    n = 0
    for _ in res:
        n += 1
    for i in range(n):
        for j in range(0, n - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res, n

def second_largest(arr):
    s, n = _sort(arr)
    return s[n - 2]

def min_max_diff(arr):
    s, n = _sort(arr)
    return s[n - 1] - s[0]

def median(arr):
    s, n = _sort(arr)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2

def min_max_array(arr):
    s, n = _sort(arr)
    return [s[0], s[n - 1]]

def to_string(arr):
    result = ""
    first = True
    for x in arr:
        if not first:
            result += "-"
        result += str(x)
        first = False
    return result