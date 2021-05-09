arr = list(map(int, input().rstrip().split()))
arr.sort()
ans = [0,0]
for i in range(4):
    ans[0] += arr[i]
for i in range(1,5):
    ans[1] += arr[i]
print(*ans)