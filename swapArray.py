n = int(input())
arr = list(map(int, input().rstrip().split()))
swaps = 0
# method 1
for i in range(n):
    if arr[i] == i+1:
        continue
    index = arr.index(i + 1)
    arr[index],arr[i] = arr[i],arr[index]
    swaps += 1

# method 2  (Interestingly, time of this method is less than above)
# for i in range(n):
#     while arr[i] != (i+1):
#             value = arr[i]-1
#             arr[i], arr[value] = arr[value], arr[i]
#             swaps+=1
print(swaps)