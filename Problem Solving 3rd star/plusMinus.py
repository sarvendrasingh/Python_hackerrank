n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
p = 0
m = 0
z = 0
for i in arr:
    if i != 0:
        if i > 0:
            p += 1
        else:
            m += 1
    else:
        z += 1
rp = p/n
rm = m/n
rz = z/n
print('{0:.6f}'.format(rp))
print('{0:.6f}'.format(rm))
print('{0:.6f}'.format(rz))