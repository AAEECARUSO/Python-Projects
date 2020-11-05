
#########################################################
# THIS IS THE SOLUTION USING FUNCTIONAL PROGRAMMING
#########################################################

solutions = 0
B = list()


def sols(board):
    global n, solutions, B

    B.append(board)
    solutions += 1


def func(board, row, col):
    global n
    for i in range(col):
        if (board[row][i]):
            return(False)
    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            return(False)
        i -= 1
        j -= 1

    i = row
    j = col
    while j >= 0 and i < n:
        if(board[i][j]):
            return(False)
        i = i + 1
        j = j - 1

    return True


def solver(board, col):
    global n
    if (col == n):
        sols(board)
        return(True)

    res = False
    for i in range(n):
        if (func(board, i, col)):
            board[i][col] = 1
            res = solver(board, col + 1) or res
            board[i][col] = 0
    return res


def solve():
    global n
    board = [[0 for j in range(n)] for i in range(n)]
    if not solver(board, 0):
        print("No Solution")
        return
    return


n = 8
solve()

print("There are {} solutions".format(len(B)))
