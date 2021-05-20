n = int(input().strip())
s = list(map(int, input().rstrip().split()))
first_multiple_input = input().rstrip().split()
d = int(first_multiple_input[0])
m = int(first_multiple_input[1])
ans = 0
for i in range(n-(m-1)):
    # print("i",i)
    bar = 0
    for j in range(i,i+m):
        # print("j",j)
        bar += s[j]
    if bar == d:
        ans += 1
print(ans)