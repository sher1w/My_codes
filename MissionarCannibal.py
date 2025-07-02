
# Check if state is safe (missionaries are never outnumbered by cannibals)

def is_safe(ml, cl, mr, cr):
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:  # taking care of the next case ig
        return False
    if (ml > 0 and cl > ml) or (mr > 0 and cr > mr):
        return False
    return True

def dfs_missionaries_and_cannibals(start, goal):
    stack = [(start, [])]  # Each item = (current_state, path_so_far)
    visited = set()
    while stack:
        state, path = stack.pop()
        ml, cl, boat = state  # ml = missionaries left, cl = cannibals left
        mr, cr = 3 - ml, 3 - cl  # right side = total - left side
        if state == goal:
            return path + [state]  # found solution
        if state in visited:
            continue
        visited.add(state)
        # All possible moves: (m, c)
        moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]

        for m, c in moves:
            if boat == 0:  # boat on left side
                next_ml = ml - m
                next_cl = cl - c
                next_boat = 1
            else:  # boat on right side
                next_ml = ml + m
                next_cl = cl + c
                next_boat = 0

            next_state = (next_ml, next_cl, next_boat)
            next_mr = 3 - next_ml
            next_cr = 3 - next_cl

            if is_safe(next_ml, next_cl, next_mr, next_cr) and next_state not in path:
                stack.append( (next_state, path + [state]) )

    return None  # no solution found

# Initial state: 3 missionaries, 3 cannibals, boat on left (0)
start = (3, 3, 0)
goal = (0, 0, 1)  # All moved to right side and boat on right

solution = dfs_missionaries_and_cannibals(start, goal)

if solution:
    print("Solution found!\n")
    for step in solution:
        print(step)
else:
    print("No solution found.")
