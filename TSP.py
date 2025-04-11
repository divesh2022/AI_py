import itertools

# Define the graph as a dictionary (adjacency matrix)
graph = {
    0: {1: 29, 2: 20, 3: 21, 4: 16, 5: 31, 6: 100, 7: 12, 8: 4, 9: 31},
    1: {0: 29, 2: 15, 3: 29, 4: 28, 5: 40, 6: 72, 7: 21, 8: 29, 9: 41},
    2: {0: 20, 1: 15, 3: 17, 4: 18, 5: 35, 6: 50, 7: 25, 8: 14, 9: 24},
    3: {0: 21, 1: 29, 2: 17, 4: 19, 5: 37, 6: 60, 7: 22, 8: 16, 9: 33},
    4: {0: 16, 1: 28, 2: 18, 3: 19, 5: 26, 6: 48, 7: 20, 8: 10, 9: 25},
    5: {0: 31, 1: 40, 2: 35, 3: 37, 4: 26, 6: 30, 7: 50, 8: 28, 9: 36},
    6: {0: 100, 1: 72, 2: 50, 3: 60, 4: 48, 5: 30, 7: 70, 8: 90, 9: 80},
    7: {0: 12, 1: 21, 2: 25, 3: 22, 4: 20, 5: 50, 6: 70, 8: 15, 9: 35},
    8: {0: 4, 1: 29, 2: 14, 3: 16, 4: 10, 5: 28, 6: 90, 7: 15, 9: 12},
    9: {0: 31, 1: 41, 2: 24, 3: 33, 4: 25, 5: 36, 6: 80, 7: 35, 8: 12},
}

# Number of cities
num_cities = len(graph)

# Function to calculate the total distance of a path
def calculate_path_distance(path):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    # Add the distance to return to the starting city
    distance += graph[path[-1]][path[0]]
    return distance

# Solve TSP using brute-force
def solve_tsp():
    cities = list(graph.keys())
    min_distance = float('inf')
    best_path = None

    # Generate all permutations of cities
    for perm in itertools.permutations(cities):
        current_distance = calculate_path_distance(perm)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = perm

    return best_path, min_distance

# Main function
if __name__ == "__main__":
    best_path, min_distance = solve_tsp()
    print("Best Path:", best_path)
    print("Minimum Distance:", min_distance)
