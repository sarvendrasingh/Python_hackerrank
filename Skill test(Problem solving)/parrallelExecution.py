files_count = int(input("Number of files: ").strip())
files = []
print("Enter Pages in file: ")
for _ in range(files_count):
    files_item = int(input().strip())
    files.append(files_item)
numCores = int(input("Number of Cores: ").strip())
limit = int(input("Enter the limit of Files to be executed parallely: ").strip())
res = 0
files.sort(reverse=True)
for i in files:
    if i%numCores == 0 and limit > 0:
        limit -= 1
        i = i/numCores
    res += i
print("Minimum time taken to execute: ")
print(int(res))



