from collections import deque

def bfs_water_jug(cap1, cap2, target1, target2=None):
    visited = set()
    queue = deque()
    queue.append(((0, 0), []))  # Each element is ((jug1, jug2), path)

    while queue:
        (jug1, jug2), path = queue.popleft()

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # Add current state to path
        path = path + [(jug1, jug2)]

        # Check if we reached the target
        if jug1 == target1 and (target2 is None or jug2 == target2):
            return path

        # Possible next states
        next_states = [
            (cap1, jug2),  # Fill jug1
            (jug1, cap2),  # Fill jug2
            (0, jug2),     # Empty jug1
            (jug1, 0),     # Empty jug2

            # Pour jug1 -> jug2
            (jug1 - min(jug1, cap2 - jug2), jug2 + min(jug1, cap2 - jug2)),

            # Pour jug2 -> jug1
            (jug1 + min(jug2, cap1 - jug1), jug2 - min(jug2, cap1 - jug1))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    return None  # No solution

# Format the steps nicely
def print_solution(path):
    for step in path:
        print(f"Jug1: {step[0]}, Jug2: {step[1]}")
    print("🎯 Reached target!")

# Get input
cap1 = int(input("Capacity of Jug1: "))
cap2 = int(input("Capacity of Jug2: "))
target1 = int(input("Target for Jug1: "))
target2_input = input("Target for Jug2 (press Enter if not needed): ")

# Convert second target if entered
target2 = int(target2_input) if target2_input.strip() else None

# Validate
if target1 > cap1 or (target2 is not None and target2 > cap2):
    print("❌ Target can't be greater than jug capacity.")
elif target1 < 0 or (target2 is not None and target2 < 0):
    print("❌ Target can't be negative.")
else:
    path = bfs_water_jug(cap1, cap2, target1, target2)
    if path:
        print("\n✅ Solution found:")
        print_solution(path)
    else:
        print("\n❌ No solution found.")
