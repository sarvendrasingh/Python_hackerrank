a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
ans = [0,0]
for i in range(len(a)):
    if a[i] > b[i]:
        ans[0] += 1
    elif b[i] > a[i]:
        ans[1] += 1
print(*ans)

