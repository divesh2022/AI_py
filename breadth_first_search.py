# Write a program to implement breadth-first search algorithm. 

def breadth_first_search(edges, vertices, num_edges, num_vertices, start, stop):
    queue = []
    visited = set()
    front = 0
    rear = -1
    key, key1 = -1, -1

    for i in range(num_edges):
        if edges[i] == start:
            key = i
        if edges[i] == stop:
            key1 = i

    rear += 1
    queue.append(edges[key])
    visited.add(edges[key])

    print("The path is:")

    while front <= rear:
        if queue[front] == stop:
            print(f"final state:\n {stop} The element is found")
            break

        print(queue[front], end=" ")
        current_vertex = edges.index(queue[front])
        front += 1

        for i in range(num_vertices):
            if vertices[current_vertex][i] == 1 and edges[i] not in visited:
                rear += 1
                queue.append(edges[i])
                visited.add(edges[i])
        print()

if __name__ == "__main__":
    print("breadth first search")
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
            print(f" [ {edge[i]} ] and [ {edge[j]} ]  = {vertices[i][j]} , ", end="")
        print()

    breadth_first_search(edge, vertices, 5, 5, 1, 4)

    print("The graph of res is:")
    for i in range(5):
        for j in range(5):
            print(f" [ {res[i]} ] and [ {res[j]} ]  = {vertices[i][j]} , ", end="")
        print()

    breadth_first_search(res, vertices, 5, 5, 'A', 'C')

