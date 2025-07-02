def best_first_search(graph, start, goal):
    open_list = {start: graph[start]['heuristic']}  # open_list: {node: heuristic}
    closed_list = []
    path = []
    while open_list:

        # Pick node with the lowest heuristic
        current = min(open_list, key=open_list.get)

        del open_list[current]

        closed_list.append(current)

        path.append(current)

        if current == goal:
            print("Goal found!")
            print("Traversal order:", " -> ".join(closed_list))  
            print("Path to goal:", " -> ".join(path))
            return

        # Add neighbors to open_list
        for neighbor, h_value in graph[current]['neighbors'].items():  # .tems because  a ictionary with in a diitoort
            if neighbor not in closed_list:
                open_list[neighbor] = h_value  # in best open_list is a ditionary not a list so u cannot apped
                

    print("Goal not found.")
    print("Traversal order:", " -> ".join(closed_list))


# ---------- INPUT SECTION ----------

graph = {}
n = int(input("Enter number of states: "))

for _ in range(n):
    state = input("Enter state name: ").upper().strip()
    heuristic = int(input(f"Enter heuristic value for {state}: "))
    neighbors_input = input(f"Enter neighbors of {state} (space-separated): ").upper().split()  

    neighbors = {}

    for neighbor in neighbors_input:
        h = int(input(f"Enter heuristic value for neighbor {neighbor}: "))
        neighbors[neighbor] = h

    graph[state] = {'heuristic': heuristic, 'neighbors': neighbors}
start_state = input("Enter starting state: ").upper().strip()
goal_state = input("Enter goal state: ").upper().strip()

# ---------- CALLING SEARCH FUNCTION ----------

if start_state == goal_state:
    print("Start and goal are the same!")
    print("Traversal order:", start_state)
    print("Path to goal:", start_state)
else:
    best_first_search(graph, start_state, goal_state)
