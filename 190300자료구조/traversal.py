class Graph:
    # 인접 리스트: 2차원 배열(리스트)로 준비, 버텍스 개수만큼
    def __init__(self, numOfVertex):
        self.graph = []
        for i in range(numOfVertex):
            self.graph.append([])

    # 버텍스 u와 v를 연결하는 에지, 즉 graph[u] 번째 리스트에 v를 추가
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # depth first search. 콘솔에서 호출
    def dfs(self):
        numOfVertex = len(self.graph)
        visited = [False] * numOfVertex
        for i in range(numOfVertex):
            if visited[i] == False:
                self.dfsRecur(i, visited)

    # recursive 함수 호출을 위한 depth first search 함수
    def dfsRecur(self, vertex, visited):
        visited[vertex] = True
        print(vertex)
        for i in self.graph[vertex]:
            if visited[i] == False:
                self.dfsRecur(i, visited)

    # breadth first search
    def bfs(self):
        numOfVertex = len(self.graph)
        visited = [False] * numOfVertex
        for i in range(numOfVertex):
            if visited[i] == False:
                self.bfsEach(i, visited)

    # 각 버텍스별 bfs 함수
    def bfsEach(self, vertex, visited):
        queue = []
        visited[vertex] = True
        queue.append(vertex)
        while len(queue) != 0:
            v = queue.pop(0)
            print(v)
            for w in self.graph[v]:
                if visited[w] == False:
                    visited[w] = True
                    queue.append(w)

    def printGraph(self):
        print(self.graph)


g = Graph(10)
g.addEdge(0, 2)
g.addEdge(0, 1)
g.addEdge(1, 3)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(2, 0)
g.addEdge(3, 9)
g.addEdge(3, 8)
g.addEdge(3, 2)
g.addEdge(3, 1)
g.addEdge(4, 5)
g.addEdge(5, 7)
g.addEdge(5, 6)
g.addEdge(5, 4)
g.addEdge(6, 7)
g.addEdge(6, 5)
g.addEdge(7, 6)
g.addEdge(7, 5)
g.addEdge(8, 3)
g.addEdge(9, 3)

print("========== 그래프 인접리스트 ===========")
g.printGraph()
print("========== DFS ===========")
g.dfs()
print("========== BFS ===========")
g.bfs()