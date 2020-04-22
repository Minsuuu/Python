class SList:
    class Node:
        def _init_(self, data, link):
            self.data = data
            self.next = link

        def _init_(self):
            self.head = None #self.head는 첫 번째 노드를 가리킴

        #가정:새 노드는 맨 뒤에 삽입
        def insert(self, data):
            new_node = self.Node(data, None)

            if self.head == None:
                self.head = new_node;
                return
            else:
                p = self.head
                while p.next != None:
                    p = p.next
                p.next = new_node

        #가정:맨 뒤 노드를 삭제
        def delete(self):
            p = self.head

            while p.next.next != None:
                p = p.next
            p.next = None

        def print_list(self):
            p = self.head
            while p != None:
                print(p.data)
                p = p.next

        def search(self, data):
            p = self.head
            while p != self.tail:
                if p.data == data:
                    print(p.data)
                p = p.next


