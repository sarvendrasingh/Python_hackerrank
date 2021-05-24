# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

# center of magic matrix is always 5. And sum is 15(row,coloumn,diagonals)
# also, diagonal should be 8,5,2 or 6,5,4 only
# 1,3,7,9 can only take positions east, west, north or south

def formingMagicSquare(s):
    # each row of magic_mat is a magic matrix itself
    # and only these 8 combinations are possible to create magic matrix
    magic_mat = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    min_cost = 81
    for k in range(8):
        crt_cost = 0
        for i in range(3):
            for j in range(3):
                crt_cost += abs(s[i][j] - magic_mat[k][i][j])
        if crt_cost < min_cost:
            min_cost = crt_cost
    return min_cost


if __name__ == '__main__':
    s = []
    print("Enter 3*3 matrix: ")
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
    print("Minimum cost required to make it magic matrix is: "+str(result) + '\n')