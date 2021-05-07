s = input()
n = int(input().strip())
count = 0
for i in s:
    if i == 'a':
        count = count + 1
r = len(s)
mod = n % r
rep = n // r
count = rep * count
for i in range(mod):
    if s[i] == 'a':
        count = count + 1
print(count)