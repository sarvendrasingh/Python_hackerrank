first_multiple_input = input("Enter x1 v1 x2 v2 respectively: ").rstrip().split()
x1 = int(first_multiple_input[0])
v1 = int(first_multiple_input[1])
x2 = int(first_multiple_input[2])
v2 = int(first_multiple_input[3])

ans = False
if x1<x2 :
    if v2<v1:
        while x1 <= x2:
            if x1 == x2:
                ans = True
                break
            x1 = x1 + v1
            x2 = x2 + v2

else :
    if x1 != x2:
        if v2>v1:
            while x2 <= x1:
                if x1 == x2:
                    ans = True
                    break
                x1 = x1 + v1
                x2 = x2 + v2
    else:
        ans = True

if ans :
    print("YES")
else:
    print("NO")