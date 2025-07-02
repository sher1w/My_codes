
def hill_climb_min(graph, start):
    current = start
    path = [current]
    while True:  # u are going to use true tst
        current_value = graph[current]['heuristic']
        neighbors = graph[current]['neighbors']
        if not neighbors:  # root node contiono
            break
        # Find best (lowest heuristic) neighbor
        next_node = current
        for neighbor in neighbors:
            if graph[neighbor]['heuristic'] < graph[next_node]['heuristic']:
                next_node = neighbor #BETTER IG
        if next_node == current:  #node does not cchnahe
            break
        current = next_node # CURRENT TAKES BETTER IG
        path.append(current)
    print("\n--- Hill Climbing Result ---")
    print("Path taken:", " -> ".join(path))
    print("Goal node (local minimum):", current)
    print("Value at goal node:", graph[current]['heuristic'])
# ---------- INPUT SECTION ----------
graph = {}
n = int(input("Enter number of states: "))

# Step 1: Get node names and heuristic values
for _ in range(n):
    state = input("Enter state name: ").upper().strip()
    heuristic = int(input(f"Enter heuristic value for {state}: "))
    graph[state] = {'heuristic': heuristic, 'neighbors': []}  # Empty neighbor list for now

# Step 2: Get neighbors for each node
for state in graph:
    neighbors = input(f"Enter neighbors of {state} (space-separated): ").upper().split()
    graph[state]['neighbors'] = neighbors 

# Step 3: Start state input
start_state = input("\nEnter starting state: ").upper().strip()

# ---------- CALLING FUNCTION ----------
hill_climb_min(graph, start_state)
