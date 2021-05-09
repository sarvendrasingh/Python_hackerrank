def check(x):
    # Returns true if x is a power of 2
    return x and (not (x & (x - 1)))


def countPairs(a):
    count = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if check(a[i] & a[j]):
                count += 1
    return count


arr_count = int(input().strip())
arr = []
for _ in range(arr_count):
    arr_item = int(input().strip())
    arr.append(arr_item)
result = countPairs(arr)

print(result)
