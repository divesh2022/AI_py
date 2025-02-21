#include <iostream>
using namespace std;

struct SparseMatrix {
    int row;
    int col;
    int value;
} sparse_matrix[100];


int** create_2d_array(const int rows, const int cols)
{
    int** c = new int*[rows];
    for (int i = 0; i < rows; ++i) {
        c[i] = new int[cols];
    }
    return c;
}

// breadth first search
template <typename T>
void breadth_first_search(T edges[], int** vertices, int num_edges, int num_vertices, T start, T stop) {
    // create a queue
    T queue[100];
    // create a visited array
    T visited[100];
    int front = 0; // Initialize front
    int rear = -1; // Initialize rear
    int visited_index = 0; // Index to track visited nodes
    // insert the start node in the queue
    int key = -1, key1 = -1;

    for (int i = 0; i < num_edges; i++) {
        if (edges[i] == start) {
            key = i;
        }
        if (edges[i] == stop) {
            key1 = i;
        }
    }
    rear = rear + 1;
    queue[rear] = edges[key]; // Use key to access the correct element
    visited[visited_index++] = edges[key]; // Use key to access the correct element

    cout<<"The path is: \n";
    // while the queue is not empty
    while (front <= rear) {
        // check if the element is the stop element
        if (queue[front] == stop) {
            cout << "final state :\n " << stop << " The element is found\n";
            break;
        }
        // remove the front element from the queue
        cout << queue[front] << " ";
        front = front + 1;
        // check the adjacent elements of the front element
        int current_vertex = -1;
        for (int i = 0; i < num_edges; i++) {
            if (edges[i] == queue[front - 1]) {
                current_vertex = i;
                break;
            }
        }
        for (int i = 0; i < num_vertices; i++) {
            if (vertices[current_vertex][i] == 1) {
                // check if the element is visited
                int flag = 0;
                for (int j = 0; j < visited_index; j++) {
                    if (edges[i] == visited[j]) {
                        flag = 1;
                    }
                }
                if (flag == 0) {
                    rear = rear + 1;
                    queue[rear] = edges[i];
                    visited[visited_index++] = edges[i];
                }
            }
        }
        cout<< endl;
    }
}

int main() {
    cout << "breadth first search\n";
    int edge[5] = {1, 2, 3, 4, 5};
    cout << "Enter the number of rows and columns: ";
    int row, col;
    cin >> row;
    cin >> col;
    int** c = create_2d_array(row, col);
    cout << "Enter the number of non-zero elements: ";
    int num;
    cin >> num;

    cout << "Enter the elements: \n";
    for (int i = 0; i < num; i++) {
        cout << "Enter the row: ";
        cin >> sparse_matrix[i].row;
        cout << "Enter the column: ";
        cin >> sparse_matrix[i].col;
        cout << "Enter the value: ";
        cin >> sparse_matrix[i].value;
    }
       // Initialize adjacency matrix with zeros
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            c[i][j] = 0;
        }
    }

    // Populate adjacency matrix with sparse matrix values
    for (int k = 0; k < num; k++) {
        int a = sparse_matrix[k].row -1 ;
        int b = sparse_matrix[k].col -1;
        c[a][b] = sparse_matrix[k].value;
    }

    cout << "Sparse matrix is: \n";
    cout << "row col value\n";
    for (int i = 0; i < num; i++) {
        cout << sparse_matrix[i].row << " " << sparse_matrix[i].col << " " << sparse_matrix[i].value << "\n";
    }

    cout << "The adjacency matrix is: \n";
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            cout << c[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "The graph of edge is: \n";
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cout <<" [ " << edge[i] << " ] and [ " << edge[j] << " ]  = " << c[i][j] << " , ";
        }
        cout << endl;
    }
    breadth_first_search(edge, c, 5, 5, 1, 4);

    char res[5] = {'A', 'B', 'C', 'D', 'E'};

    cout << "The graph of res is: \n";
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cout <<" [ " << res[i] << " ] and [ " << res[j] << " ]  = " << c[i][j] << " , ";
        }
        cout << endl;
    }
    breadth_first_search<char>(res, c, 5, 5, 'A', 'C');

    return 0;
}
