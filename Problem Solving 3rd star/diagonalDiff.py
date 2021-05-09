n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
principal = 0
secondary = 0
for i in range(n):
    for j in range(n):
        if i == j:
            principal += arr[i][j]
        if (i + j) == (n - 1):
            secondary += arr[i][j]
ans = 0
if principal > secondary:
    ans = principal - secondary
else:
    ans = secondary - principal
print(ans)