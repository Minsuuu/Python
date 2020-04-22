class GraphWeighted:
    def __init__(self, vertices):
        self.V = vertices
        # 인접 리스트 graph: 1차원 배열. 각 원소는 에지, 즉 (u, v, w) 튜플. u, v는 버텍스, w는 에지의 weight
        self.graph = []
    # 버텍스 u와 v를 연결하는 에지 추가, w는 에지의 weight
    def addEdge(self, u, v, w):
        self.graph.append((u, v, w))
    def kruskal(self):
        mst = []    # 결과값. mst를 구성하는 에지들만 포함
        edges = 0   # 현재 mst에 포함된 에지 수
        self.graph.sort(key=self.keyFunction)   # 인접리스트의 에지들을 가중치의 오름차순으로 정렬
        parent = [] # 버텍스들의 상호 배타적 집합, 각 인덱스(즉 버텍스 번호)의 값은 그 집합의 root 버텍스
        for i in range(self.V): # parent 배열 초기화
            parent.append(i)
        while edges < self.V - 1:
            u, v, w = self.graph.pop(0)     # 남은 에지들 중 가중치가 최소인 것을 가져온다.
            if self.find(parent, u) != self.find(parent, v):    # 에지의 두 버텍스가 서로 다른 집합에 속해 있으면
                mst.append((u, v, w))       # 그 에지를 mst에 추가하고
                edges = edges + 1           # mst에 추가된 에지 수를 1 증가시키고
                self.union(parent, u, v)    # 두 버텍스의 집합을 합한다.
        return mst
    # parent 배열에서 버텍스 v가 속한 집합의 루트 버텍스 찾기
    def find(self, parent, v):
        if parent[v] == v:
            return v
        else:
            return self.find(parent, parent[v])
    # 버텍스 u가 속한 집합과 v가 속한 집합을 합치기
    def union(self, parent, u, v):
        root1 = self.find(parent, u)
        root2 = self.find(parent, v)
        parent[root1] = root2
    # self.graph를 정렬할 때 기준값을 정하는 함수, 기준값은 각 튜플 (u, v, w)에서 가중치인 w
    def keyFunction(self, e):
        return e[2]
    # 그래프 출력해보기
    def printGraph(self):
        print(self.graph)
g = GraphWeighted(7)
g.addEdge(0, 1, 9)
g.addEdge(0, 2, 10)
g.addEdge(1, 3, 10)
g.addEdge(1, 4, 5)
g.addEdge(1, 6, 3)
g.addEdge(2, 3, 9)
g.addEdge(2, 4, 7)
g.addEdge(2, 5, 2)
g.addEdge(3, 5, 4)
g.addEdge(3, 6, 8)
g.addEdge(4, 6, 1)
g.addEdge(5, 6, 6)
g.printGraph()
mst = g.kruskal()
print(mst)