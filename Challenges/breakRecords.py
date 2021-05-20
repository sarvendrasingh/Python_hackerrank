n = int(input())
l = list(map(int, input().strip().split(" ")))
low =[]
high =[]
for i in range(n):
    if i != 0:
        s1 = len(low)
        s2 = len(high)
        if low[s1-1]>l[i]:
            low.append(l[i])
        if high[s2-1]<l[i]:
            high.append(l[i])
    else:
        low.append(l[i])
        high.append(l[i])
print(len(high)-1,len(low)-1)
