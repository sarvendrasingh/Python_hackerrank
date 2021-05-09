first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
queries = []
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
l = [0] * n
for i in range(m):
    for j in range(queries[i][0]-1,queries[i][1]):
        l[j] = l[j] + queries[i][2]
res = max(l)
print(res)