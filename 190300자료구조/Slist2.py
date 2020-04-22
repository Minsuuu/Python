class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link
    def __init__(self):
        self.head = None
    # 가정: 새 노드를 맨 뒤에 삽입
    def insert(self, item):
        n = self.Node(item, None)
        if self.head == None:
          self.head = n
          return
        p = self.head
        while p.next != None:
            p = p.next
        p.next = n
    # 가정: 맨 뒤의 노드를 삭제
    def delete(self):
        p = self.head
        while p.next.next != None:
            p = p.next
        p.next = None
    def print_list(self):
        p = self.head
        while p != None:
            print(p.item)
            p = p.next
s = SList()
s.insert(30)
s.insert(40)
s.insert(50)
s.insert(60)
s.print_list()
s.delete()
s.print_list()