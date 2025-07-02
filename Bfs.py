def bfs(graph, start, goals):
    queue = [start]
    visited = []
    parent = {start: None}

    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.append(node)

        if node in goals:
            print("\nBFS Traversal:")
            print(" -> ".join(visited))

            # Print path from start to goal
            path = []
            while node:
                path.append(node)
                node = parent[node]
            path.reverse()

            print("\nShortest Path:", " -> ".join(path))
            return

        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                queue.append(neighbor)
                parent[neighbor] = node

    print("No goal found!")

# --- INPUT SECTION ---
graph = {}
n = int(input("How many states? "))

for _ in range(n):
    state = input("Enter state name: ").upper()
    neighbours = input(f"Neighbours of {state}: ").upper().split()
    graph[state] = neighbours

start = input("Enter start state: ").upper()
goals = input("Enter goal states (space separated): ").upper().split()

bfs(graph, start, goals)
