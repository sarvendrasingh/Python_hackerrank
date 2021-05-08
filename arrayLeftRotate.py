first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
a = list(map(int, input().rstrip().split()))

# method 1

flag = a[0]
for i in range(d):
    for j in range(n-1):
        a[j] = a[j+1]
    a[n-1] = flag
    flag = a[0]

# method 2

# a = a[d:]+a[:d]

# output
for i in range(n):
    print(a[i],end=" ")