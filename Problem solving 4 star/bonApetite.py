#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#


def bonAppetit(bill, k, b):
    bill.pop(k)
    sum = 0
    for i in bill:
        sum += i
    anna = sum // 2
    if b > anna:
        print("Extra amount charged: "+str(b - anna))
    else:
        print('Bon Appetit(Correct amount charged)')


if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()
    # n = int(first_multiple_input[0])
    # k = int(first_multiple_input[1])

    n = int(input("Enter number of items: "))
    k = int(input("Enter index of item that Anna didnt eat: "))
    bill = list(map(int, input("Enter price of each item seperated by space: ").rstrip().split()))
    b = int(input("Enter amount Anna was charged: ").strip())

    bonAppetit(bill, k, b)
