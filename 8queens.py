import random

def attacks(board, row, col, n):
    count = 0
    for c in range(n):
        if c == col:
            continue
        r = board[c]
        if r == row or abs(r - row) == abs(c - col):
            count += 1
    return count

def solve(board, n):
    for step in range(100):
        
            # jaldi 5
        
        
        # time lagega bhidu
        conflict = []
        for c in range(n):
            if attacks(board, board[c], c, n) > 0:
                conflict.append(c)
        if not conflict:
            return board
        c = random.choice(conflict)
        
        min_val = n
        best = []
        for r in range(n):
            a = attacks(board, r, c, n)
            if a < min_val:
                min_val = a
                best = [r]
            elif a == min_val:
                best.append(r)
        board[c] = random.choice(best)
    return None

# ---------- MAIN ----------
n = int(input("Enter number of queens: "))
board = []

print("Enter row for each column (starting position):")
for i in range(n):
    row = int(input(f"Column {i}: "))
    board.append(row)
result = solve(board, n)

if result:
    print("\n✅ Queen positions (column : row):")
    for i in range(n):
        print(f"Column {i} → Row {result[i]}")
else:
    print("❌ No solution found.")
