import copy
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]  # 0 = blank tile

# Heuristic: count of misplaced tiles
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# Find position of blank (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighbors by moving the blank tile
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors


def hill_climb(start):
    current=start
    h=heuristic(start)
    path=[current]
    while True:    #  keep running this bro until break statemn such as not better soliton or goal is rached 
        neighbours=get_neighbors(current)  # get all neighbours in one shot list for the urrent 
        next_state=None
        best_h=h        
        for neighbour in neighbours:
            if best_h > heuristic(neighbour):
                next_state=neighbour
                best_h=heuristic(neighbour)
        if next_state is None: # no better solution so stops ig  i.e for loop above is ineffective 
                break
        current=next_state   # here there is  a better solution  strategticly placed  
        h=best_h
        path.append(current)         #
        if current == goal:
            break
    return path 

 # here return path is last because it has to be retured in any case bro 
# Example start state
start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

solution = hill_climb(start)

if solution[-1] == goal:   # -1 stands for last step huh
    print("✅ Goal reached in", len(solution)-1, "moves!")
else:
    print("⚠️ Local maximum reached. Goal not found.")
    
print("\nPath:")
for step in solution:
    for row in step:
        print(row)
    print("-----")