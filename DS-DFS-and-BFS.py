# make adjacent matrix
# using input nodes, edges to make adjacent matrix
def make_adjMatrix(nodes, edges):
    # make empty adj_matrix by nodes * nodes 
    adj_matrix = []
    for _ in range(len(nodes)):
        line = []
        for _ in range(len(nodes)):
            line.append(0)
        adj_matrix.append(line)

    # consider bidirectional edge(undirected graph)
    for i in range(len(edges)):
        start = edges[i][0]
        end = edges[i][1]
        adj_matrix[start][end] = 1
        adj_matrix[end][start] = 1
    return adj_matrix

# DFS function
# graph = adjacency matrix
# start = start vertex(node)
# nodes = using nodes' size 
def DFS(graph, start, nodes):
    # mark all the vertices as not visited
    visited = [False] * (len(nodes))
    DFSUtill(graph, start, visited)

# DFSUtill function    
def DFSUtill(graph, start, visited):
    # mark the current node(start)
    visited[start] = True
    print(start, end=' ')
    
    # graph[start][i] == 1 추가
    # start에서 방문할 수 있는지 여부를 추가
    for i in range(len(visited)):
        if graph[start][i] == 1 and visited[i] == False:
            DFSUtill(graph, i, visited)

# BFS function
# graph = adjacency matrix
# start = start vertex(node)
# nodes = using nodes' size 
def BFS(graph, start, nodes):
    # mark all the vertices as not visited
    visited = [False] * (len(nodes))
    # create queue for BFS
    queue = []
    queue.append(start) # Mark the start node and enqueue it
    visited[start] = True
    
    while queue:
        s = queue.pop(0) # dequeue vertex
        print(s, end=' ')
        
        for i in range(len(nodes)):
            # graph[s][i] == 1 추가
            # s에서 방문할 수 있는지 여부를 추가
            if graph[s][i] == 1 and visited[i] == False:
                queue.append(i) # mark the i node and enqueue it
                visited[i] = True


if __name__ == "__main__":
    
    print("------------HW 3-2-----------------")
    
    # allocate nodes
    nodes = list(map(int, input("input nodes : ").split()))
    
    # Edge's total #
    E = int(input("Edge's total number : "))
    
    # make edges' list
    edges = []
    for i in range(E):
        edges.append(list(map(int, input("input edges : ").split())))
    
    matrix = make_adjMatrix(nodes, edges)
    print("matrix는 이중리스트로 표현할 때 다음과 같다")
    print(matrix)
    
    print("------------------------------")
    print("DFS를 적용했을 때 : ", end = '')
    DFS(matrix, nodes[0], nodes)
    print( )
    print("-------------------------------")
    print("DFS를 적용했을 때 : ", end = '')
    BFS(matrix, nodes[0], nodes)
    
    