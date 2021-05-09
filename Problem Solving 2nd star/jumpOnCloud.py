n = int(input().strip())
c = list(map(int, input().rstrip().split()))
count = 0
i = 0
while i < n-1:
    if c[i] == 0:
        i = i + 1
    count = count + 1
    i = i + 1
print(count)