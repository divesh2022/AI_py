# Write a program to implement depth-first search algorithm. 

def depth_first_search(edges, vertices, num_edges, num_vertices, start, stop):
    stack = []
    visited = set()
    key, key1 = -1, -1

    for i in range(num_edges):
        if edges[i] == start:
            key = i
        if edges[i] == stop:
            key1 = i
    stack.append(edges[key])
    visited.add(edges[key])

    print("The path is:")

    while stack:
        current = stack.pop()
        print(current, end=" \n")

        if current == stop:
            print(f"\nfinal state:\n {stop} The element is found")
            return

        current_vertex = edges.index(current)
        for i in range(num_vertices - 1, -1, -1):
            if vertices[current_vertex][i] == 1 and edges[i] not in visited:
                stack.append(edges[i])
                visited.add(edges[i])

    print("\nThe element is not found")

if __name__ == "__main__":
    print("depth first search")
    edge = [1, 2, 3, 4, 5]
    res = ['A', 'B', 'C', 'D', 'E']
    vertices = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0]
    ]

    print("The graph of edge is:")
    for i in range(5):
        for j in range(5):
            print(f" [ {edge[i]} ] and [ {edge[j]} ] = {vertices[i][j]} , ", end="")
        print()

    depth_first_search(edge, vertices, 5, 5, 1, 4)

    print("The graph of res is:")
    for i in range(5):
        for j in range(5):
            print(f" [ {res[i]} ] and [ {res[j]} ] = {vertices[i][j]} , ", end="")
        print()

    depth_first_search(res, vertices, 5, 5, 'A', 'C')
