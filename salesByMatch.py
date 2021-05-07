n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
pair = 0
l=[]
for i in range(0,n):
    if ar[i] in l:
        l.remove(ar[i])
        pair=pair+1
    else:
        l.append(ar[i])
print(pair)
