from heapq import heappush, heappop
graph = {}
heuristic = {}
# Input graph
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ").upper()
    graph[node] = []
    m = int(input(f"Enter number of neighbors of {node}: "))
    for _ in range(m):
        nbr, cost = input("Enter neighbor and cost (space-separated): ").upper().split()
        graph[node].append((nbr, int(cost)))
        print(graph)
# Input heuristic values
h = int(input("Enter number of heuristic values: "))
for _ in range(h):
    node, hval = input("Enter node and heuristic value (space-separated): ").upper().split()
    heuristic[node] = int(hval)
start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

# A* Search
open_list = []
heappush(open_list, (heuristic[start], 0, start, [start]))  # (f, g, node, path)
closed = set()
found = False

while open_list:
    f, g, node, path = heappop(open_list)

    if node == goal:
        print("Path found!")
        print("Path Cost:", g)
        print("Path:", " -> ".join(path))
        found = True
        break

    if node in closed:
        continue
    closed.add(node)

    for neighbor, cost in graph[node]:
        if neighbor not in closed:
            g_new = g + cost
            f_new = g_new + heuristic[neighbor]
            heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

if not found:
    print("No path found.")
