import copy 
goal=[ [1,2,3],
[4,5,6],
[7,8,0]]

def heuristic(state):
    count=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=goal[i][j] and state[i][j] !=0: 
              count+=1
              #print(state[i][j], count)
    return count

def find_blank(state):
     for i in range(3):
        for j in range(3):
            if state[i][j]== 0:
                return i,j
            
def get_neighbours(state):
    neighbours = []
    # Find the position of the blank (0)
    x, y = find_blank(state)
    # Define 4 possible directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Try each direction
    for dx, dy in directions:
        nx, ny = x + dx, y + dy  # New position after move
        # Check if new position is inside the 3x3 board
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Make a copy of the state
            new_state = []
            new_state = copy.deepcopy(state)
              # Copy each row
            # Swap blank with neighbor
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            # Add the new state to the list of neighbors
            neighbours.append(new_state)
    return neighbours


def best_first(start):
    queue=[(heuristic(start),start,[start])]
    visited=[]
    while queue:
        queue.sort()  # brst bro first sort 
        h,current,path=queue.pop(0)
        if current==goal:
            return path
        visited.append(current)
        for neighbour in get_neighbours(current):
            if neighbour not in visited:
                queue.append((heuristic(neighbour),neighbour,path + [neighbour]))
    return path

# Example usage
start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]
solution = best_first(start)
# Show steps
if solution:
    print("Steps to reach goal:")
    for step in solution:
        for row in step:
            print(row)
        print("-----")
else:
    print("No solution found.")