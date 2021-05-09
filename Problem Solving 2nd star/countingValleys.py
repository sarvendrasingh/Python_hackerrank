steps = int(input().strip())
path = input()
valley=0
current=0
gaddha = False
myDict={"U":1,"D":-1}
for i in range(steps):
    current = current + myDict[path[i]]
    if current == -1:
        gaddha = True
    if gaddha:
        if current == 0:
            valley = valley + 1
            gaddha = False
print(valley)
