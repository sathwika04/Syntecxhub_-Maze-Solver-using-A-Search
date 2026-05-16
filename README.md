# Syntecxhub_-Maze-Solver-using-A*-Search


This project implements a Maze Solver using the A* (A-Star) Search Algorithm in Python. The program finds the shortest possible path between a start node and a goal node while avoiding obstacles (walls) in the maze.

The project also provides a graphical visualization of the maze, explored path, start position, and goal position using Matplotlib.

---

## Features

- Implements the A* Search Algorithm
- Uses Manhattan Distance Heuristic
- Finds the shortest path efficiently
- Handles unreachable path cases
- Visualizes maze and final solution path
- Beginner-friendly Artificial Intelligence project

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- Heapq (Priority Queue)

---

## How It Works

1. The maze is represented as a 2D grid:
   - `0` → Free path
   - `1` → Wall/Obstacle

2. A* Search uses:
   - `g(n)` → Distance from start node
   - `h(n)` → Heuristic distance to goal
   - `f(n) = g(n) + h(n)`

3. The algorithm explores the optimal path with minimum cost.

---

## Heuristic Used

### Manhattan Distance

```python
abs(x1 - x2) + abs(y1 - y2)

This heuristic works efficiently for grid-based movement.

Project Structure
maze_solver.py
README.md
Installation

Install required libraries:

pip install matplotlib numpy
Run the Project
python maze_solver.py
Output
Displays the shortest path coordinates
Shows graphical maze visualization
Visualization Colors
Black → Walls
White → Open Path
Blue → Shortest Path
Green → Start Node
Red → Goal Node
Example Use Cases
Pathfinding systems
Robotics navigation
Game AI
Artificial Intelligence learning
Search Algorithms demonstration
Future Improvements
Add diagonal movement
Real-time animation of search process
Random maze generation
GUI-based interactive maze editor
Compare BFS, DFS, and A* performance
