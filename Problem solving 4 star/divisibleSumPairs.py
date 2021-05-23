first_multiple_input = input("Enter values of n and k seperated by space: ").rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
ar = list(map(int, input("Enter array of length "+str(n)+": ").rstrip().split()))
count = 0
for i in range(n):
    for j in range(i+1,n):
        if (ar[i]+ar[j])%k == 0:
            count += 1
print("Total number of pairs that sum up to be divisible by "+str(k)+" are: "+str(count))