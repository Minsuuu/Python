# Library for maxsize
import sys
class GraphAdjMatrix():
    def __init__(self, vertices):   # 인접행렬(Adj. Matrix)로 저장하기로 함
        self.V = vertices            # 필드변수 V는 버텍스 수
        self.graph = [[0 for column in range(self.V)] for row in range(self.V)]
    def dijkstra(self, src):
        distance = [sys.maxsize] * self.V   # src 버텍스로부터 각 버텍스까지의 거리 저장
        distance[src] = 0              # src에서 src로의 거리는 0
        visited = [False] * self.V    # 방문여부 표시
        previous = [None] * self.V      # 최단경로에서 각 노드의 바로 직전 노드 저장
        previous[src] = src         # src에서 src로의 최단경로에서 src 직전 노드는 자기 자신
        for xxx in range(self.V):
            minDistance = sys.maxsize   # 방문하지 않은 버텍스 중 가장 가까운 버텍스까지의 거리
            minIndex = None             # 바로 그 가장 가까운 버텍스 번호
            for v in range(self.V):
                if distance[v] < minDistance and visited[v] == False: # 더 가까운 버텍스가 있다면
                    minDistance = distance[v]   # 그 버텍스의 거리로 업데이트하고
                    minIndex = v                # 그 버텍스 번호로 업데이트
            visited[minIndex] = True
            for v in range(self.V):
                if self.graph[minIndex][v] > 0 and visited[v] == False: # 새로 추가된 minIndex에서 v로의 에지가 있다면
                    if distance[minIndex] + self.graph[minIndex][v] < distance[v]: # 그 에지를 거치는 경로가 더 짧다면
                        distance[v] = distance[minIndex] + self.graph[minIndex][v] #   업데이트!
                        previous[v] = minIndex  # 최단경로 상에서 v의 바로 직전은 minIndex
        self.printDistance(src, distance)
        print("======================================")
        self.printPath(src, previous)
    def printDistance(self, src, distance):
        for i in range(self.V):
            print(src, i, " = ", distance[i])
    def printPath(self, src, previous):
        for i in range(self.V):
            back = i
            print(back, end="")
            while back != src:
                print(" <- ", previous[back], end="")
                back = previous[back]
            print("")
g = GraphAdjMatrix(8)
g.graph = [[0, 1, 0, 2, 0, 0, 0, 0],
            [1, 0, 4, 3, 1, 6, 0, 0],
            [0, 4, 0, 0, 0, 1, 1, 2],
            [2, 3, 0, 0, 5, 0, 0, 0],
            [0, 1, 0, 5, 0, 0, 2, 0],
            [0, 6, 1, 0, 0, 0, 0, 9],
            [0, 0, 1, 0, 2, 0, 0, 1],
            [0, 0, 2, 0, 0, 9, 1, 0]]
g.dijkstra(0)