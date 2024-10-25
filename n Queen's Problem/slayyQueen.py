def solve(board, col, n):

    if col == n:
        for row in board:
            print(row)
        return True

    for i in range(n):

        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve(board, col+1, n):
                return True
        board[i][col] = 0

    return False


def is_safe(board, row, col, n):

    # Check row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


n = 8
board = [[0 for _ in range(n)] for _ in range(n)]
solve(board, 0, n)
