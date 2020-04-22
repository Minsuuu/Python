class DList:
    class Node:
        def __init__(self, item, prev_link, next_link):
            self.item = item
            self.prev = prev_link
            self.next = next_link
            def __init__(self):
                self.head = self.Node(None, None, None)
                self.tail = self.Node(None, self.head, None)
                self.head.next = self.tail
                # 가정: 새 노드를 맨 뒤(즉 self.tail의 바로 앞)에 넣음
                def insert(self, item):
                    new_node = self.Node(item, None, None)
                    new_node.prev = self.tail.prev
                    new_node.next = self.tail
                    self.tail.prev.next = new_node
                    self.tail.prev = new_node
                #  가정: 맨 뒤(즉 self.tail의 바로 앞) 노드를 삭제
                def delete(self):
                    self.tail.prev.prev.next = self.tail
                    self.tail.prev = self.tail.prev.prev
                    def print_list(self):
                        p = self.head.next
                        while p != self.tail:
                            print(p.item)
                            p = p.next

d = DList()
d.insert(30)
d.insert(40)
d.insert(50)
d.insert(60)
d.print_list()

d.delete()
d.print_list()
