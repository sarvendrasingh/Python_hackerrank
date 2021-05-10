first_multiple_input = input("Enter location of house starting and end point seperated by space: ").rstrip().split()
s = int(first_multiple_input[0])
t = int(first_multiple_input[1])

second_multiple_input = input("Enter location of apple and orange tree respectively seperated by space: ").rstrip().split()
a = int(second_multiple_input[0])
b = int(second_multiple_input[1])

third_multiple_input = input("Enter number of apples and oranges fell seperated by space: ").rstrip().split()
m = int(third_multiple_input[0])
n = int(third_multiple_input[1])

print("Enter distance travelled by each fallen apple seperated by space: ", end=" ")
apples = list(map(int, input().rstrip().split()))
print("Enter distance travelled by each fallen orange seperated by space: ", end=" ")
oranges = list(map(int, input().rstrip().split()))

apple = 0
orange = 0
for i in apples:
    if s <= a+i <= t:
        apple += 1
for j in oranges:
    if s <= b+j <= t:
        orange += 1

print("Number of apples that fell in house: ", end=" ")
print(apple)
print("Number of oranges that fell in house: ", end=" ")
print(orange)

