import copy

# Final goal configuration
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

# Display the puzzle in 3x3 format
def print_puzzle(state):
    for row in state:
        print(row)
    print()

# Find where the blank (0) is located
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j  # Return the position of blank

# Get all valid moves (up, down, left, right)
def get_moves(state):
    x, y = find_blank(state)
    moves = []
    if x > 0: moves.append((-1, 0))  # Move up
    if x < 2: moves.append((1, 0))   # Move down
    if y > 0: moves.append((0, -1))  # Move left
    if y < 2: moves.append((0, 1))   # Move right
    return moves

# Apply a move and return new state
def apply_move(state, move):
    x, y = find_blank(state)
    new_x, new_y = x + move[0], y + move[1]
    new_state = copy.deepcopy(state)
    new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
    return new_state

# Count number of misplaced tiles (heuristic)
def count_misplaced(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# Hill Climbing Algorithm
def hill_climbing(start):
    current = start
    while True:
        print("Current State:")
        print_puzzle(current)
        h = count_misplaced(current)
        print("Heuristic (misplaced tiles):", h)

        if current == goal:
            print("🎯 Goal Reached!")
            break

        neighbors = []
        for move in get_moves(current):
            new_state = apply_move(current, move)
            neighbors.append(new_state)

        # Pick the neighbor with the lowest heuristic
        next_state = min(neighbors, key=count_misplaced)
        next_h = count_misplaced(next_state)

        # If no improvement, stop (local minimum)
        if next_h >= h:
            print("\n⚠️ Local Minimum Reached. Stuck!")
            print("Final State:")
            print_puzzle(current)
            print("Heuristic:", h)
            break

        current = next_state

# Take input from user
def input_puzzle():
    print("Enter the 3x3 puzzle state (use 0 for blank):")
    puzzle = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        puzzle.append(row)
    return puzzle

# Run the program
initial = input_puzzle()
hill_climbing(initial)
