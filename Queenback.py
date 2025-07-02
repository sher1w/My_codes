def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i] == j:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True  # solution found

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # place queen
            if solve_n_queens(board, row + 1, n):  # recurse
                return True
            board[row] = -1  # backtrack

    return False  # no solution from this row

# ----------- MAIN ------------
n = int(input("Enter number of queens: "))
board = [-1] * n  # Initialize empty board

if solve_n_queens(board, 0, n):
    print("\n✅ Queen positions (column : row):")
    for col, row in enumerate(board):
        print(f"Column {col} → Row {row}")
else:
    print("❌ No solution found.")
