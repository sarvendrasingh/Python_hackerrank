first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
arr.sort()
brr.sort()

LCM = []
for i in range(arr[0],brr[0]+1):
    add = False
    for j in arr:
        if i % j == 0:
            add = True
        else:
            add = False
            break
    if add:
        LCM.append(i)

ans = []
for i in LCM:
    add = False
    for j in brr:
        if j%i == 0:
            add = True
        else:
            add = False
            break
    if add:
        ans.append(i)


print(len(ans))
