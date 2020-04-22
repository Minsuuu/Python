class SList:
    class Node:
        def __init__(self, data, link):
            self.data = data
            self.next = link
    def __init__(self):
        self.head = None
        # self.head는 첫 번째 노드를 가리킴
    def insert(self,data):
        newNode = self.Node(data,None)
s = SList();
