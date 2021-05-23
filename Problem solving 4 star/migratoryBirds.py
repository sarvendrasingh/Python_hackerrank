arr_count = int(input("Enter number of birds: ").strip())
arr = list(map(int, input("Enter type of each bird seperated by space: ").rstrip().split()))
arr_freq = [0,0,0,0,0]
for i in arr:
    arr_freq[i-1] += 1
ans = arr_freq.index(max(arr_freq))+1
print("Maximum frequency birds was of type: "+str(ans))