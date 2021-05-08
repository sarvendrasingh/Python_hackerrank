arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
arr2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(4):
    for j in range(4):
        arr2[i][j] = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
maximum = arr2[0][0]
for i in range(4):
    for j in range(4):
        # print(arr2[i][j])
        if arr2[i][j] > maximum:
            maximum = arr2[i][j]
print(maximum)