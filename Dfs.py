def goal_test(node, goal_states):
    return node in goal_states

def dfs(graph, start, goal_states):
    stack = [start]
    visited = []
    parent = {start: None}

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.append(current)

        if goal_test(current, goal_states):
            print("\nDFS Traversal Order:")
            print(" -> ".join(visited))

            # Reconstruct path from start to goal
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()

            print("\nPath to Goal:")
            print(" -> ".join(path))
            return

        # Add neighbors in reverse order to maintain DFS order
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in parent:
                stack.append(neighbor)
                parent[neighbor] = current

    print("Goal state not found!")

# ====== MAIN DRIVER CODE ======
graph = {}
n = int(input("Enter total number of states: "))
for _ in range(n):
    state = input("Enter state: ").strip().upper()
    neighbors = input(f"Enter neighbors of {state} (space-separated): ").strip().upper().split()
    graph[state] = neighbors

start = input("Enter starting state: ").strip().upper();
goal_states = input("Enter goal state(s) (space-separated): ").strip().upper().split()

dfs(graph, start, goal_states)
