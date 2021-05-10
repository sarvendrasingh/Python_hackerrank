grades_count = int(input("Enter number of Students: ").strip())
print("Enter their grades respectively: ")
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)


def passed(marks):
    if marks > 37:
        return True
    else:
        return False


a = []
for i in grades:
    if passed(i):
        nextMultiple = i + 5 - (i % 5)
        if (nextMultiple-i) < 3:
            a.append(nextMultiple)
        else:
            a.append(i)
    else:
        a.append(i)
print("Final rounded grades are: ")
print(*a, sep="\n")
