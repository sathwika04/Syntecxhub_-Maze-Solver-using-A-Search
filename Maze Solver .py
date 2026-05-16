# Maze Solver using A* Search Algorithm
# Author: Muppalla Sathwika

import heapq
import matplotlib.pyplot as plt
import numpy as np

# Maze Representation
# 0 = Free Path
# 1 = Wall

maze = [
    [0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0],
]

start = (0, 0)
goal = (5, 6)

# Directions: Up, Down, Left, Right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Manhattan Distance Heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* Algorithm
def astar(maze, start, goal):

    rows = len(maze)
    cols = len(maze[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    visited = set()

    while open_set:

        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        visited.add(current)

        for dx, dy in directions:

            neighbor = (current[0] + dx, current[1] + dy)

            # Check boundaries
            if (0 <= neighbor[0] < rows and
                0 <= neighbor[1] < cols):

                # Skip walls
                if maze[neighbor[0]][neighbor[1]] == 1:
                    continue

                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:

                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)

                    if neighbor not in visited:
                        heapq.heappush(open_set,
                                       (f_score[neighbor], neighbor))

    return None


# Reconstruct Final Path
def reconstruct_path(came_from, current):

    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


# Visualize Maze and Path
def visualize_maze(maze, path, start, goal):

    grid = np.array(maze)

    plt.figure(figsize=(8, 6))

    # Draw maze
    plt.imshow(grid, cmap='binary')

    # Draw path
    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y, color='blue', linewidth=3, label='Path')

    # Start and Goal
    plt.scatter(start[1], start[0],
                color='green', s=100, label='Start')

    plt.scatter(goal[1], goal[0],
                color='red', s=100, label='Goal')

    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))

    plt.grid(True)
    plt.legend()
    plt.title("Maze Solver using A* Search")

    plt.show()


# Run Algorithm
path = astar(maze, start, goal)

if path:
    print("Shortest Path Found:")
    print(path)

    visualize_maze(maze, path, start, goal)

else:
    print("No path exists to the goal.")