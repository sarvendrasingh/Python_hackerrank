ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))
ans = 0
for i in ar:
    ans += i
print(ans)