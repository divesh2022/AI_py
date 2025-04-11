# Write a program to implement the Hill Climbing algorithm.

import math
def euclidean_distance(node1, node2):
    return math.sqrt((node2[0] - node1[0]) ** 2 + (node2[1] - node1[1]) ** 2)
def hill_climbing(graph, start, goal, heuristic):
    current_node = start
    visited = set()
    while current_node != goal:
        visited.add(current_node)
        neighbors = graph.get(current_node, [])
        best_neighbor = None
        best_heuristic = float('inf')
        for neighbor, _ in neighbors:
            if neighbor not in visited:
                h_value = heuristic(current_node, neighbor)
                if h_value < best_heuristic:
                    best_heuristic = h_value
                    best_neighbor = neighbor
        if best_neighbor is None:
            print("Stuck! No better neighbor found.")
            return None
        current_node = best_neighbor
        print(f"Moving to {current_node}")
    print(f"Goal {goal} reached!")
    return current_node
graph = {
    'X': [('Y', (3, 2)), ('Z', (1, 3)),('W', (2, 3))],
    'Y': [('X', (0, 0)), ('W', (2, 3)), ('Z', (1, 3))],
    'Z': [('X', (0,0)), ('W', (2,3)), ('Y', (3,2))],
    'W': [('Y', (3,2)), ('Z', (1,3)), ('X', (0,0))]
}
positions = {
    'X': (0, 0),
    'Y': (3, 2),
    'Z': (1, 3),
    'W': (2, 3)
}
def main():
    start_node = 'X'
    goal_node = 'W'
    result = hill_climbing(
        graph, start_node, goal_node, lambda n1, n2:
        euclidean_distance(positions[n1], positions[n2])
    )
    print(f"Final result: {result}")

main()
