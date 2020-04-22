def bin2dec(s):
    length = len(s)
    result = 0
    for i in range(length - 1, -1, -1):
        result += int(s[i]) * (2 ** (length - 1 - i))

    print(result)

class SList:
    class Node:
        def __init__(self, data, link):
            self.data = data
            self.next = link
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = self.Node(data, None)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def insert_last(self, data):
        new_node = self.Node(data, None)
        if self.head == None:
            self.head = new_node
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = new_node

    def search(self, data):
        s = self.head
        position = 1
        while s != None:
            if s.data == data:
                return position
            else:
                s = s.next
                position += 1
        return 0

    def print_list(self):
        s = self.head
        while s != None:
            print(s.data)
            s = s.next

class DList:
    class Node:
        def __init__(self, data, prev_link, next_link):
            self.data = data
            self.prev = prev_link
            self.next = next_link
    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail

    # 가정: 새 노드를 맨 뒤 (즉 self.tail의 바로 앞)에 넣음
    def insert_last(self, data):
        new_node = self.Node(data, None, None)
        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node

    # 가정: 맨 뒤(즉 self.tail의 바로 앞) 노드를 삭제
    def delete_last(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    # 가정: 새 노드를 맨 앞(즉 self.head의 바로 뒤)에 넣음
    def insert_first(self, data):
        new_node = self.Node(data, self.head, self.head.next)
        if self.head.next == self.tail:         # 데이터 노드가 하나도 없을 때
            self.tail.prev = new_node
            self.head.next = new_node
        else:
            self.head.next.prev = new_node
            self.head.next = new_node

    # 가정: 맨 앞(즉 self.head의 바로 뒤) 노드를 삭제
    def delete_first(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # 가정: DList가 오름차순으로 정렬되어 있다고 가정하고 새로운 데이터를 정렬이 유지되는 위치에 삽입
    def insert_sorted(self, data):
        new_node = self.Node(data, None, None)
        p = self.head.next
        if p == self.tail:          # 아직 데이터가 하나도 없을 때
            new_node.next = self.tail
            new_node.prev = self.head
            self.tail.prev = new_node
            self.head.next = new_node
        else:
            while p != self.tail:
                if p.data > data:           # 즉 새 노느, 즉 new_node를 p 바로 앞에 넣는다.
                    new_node.prev = p.prev
                    new_node.next = p
                    p.prev.next = new_node
                    p.prev = new_node
                    return
            else:
                p= p.next
            # 새로 넣을 데이터가 제일 큰 값인 경우
            new_node.prev = p.prev
            new_node.next = p
            p.prev.next = new_node
            p.prev = new_node
            return
    def print_list(self):
        p = self.head.next
        while p != self.tail:
            print(p.data)
            p = p.next
            
d = DList()
d.insert_sorted(5)
d.insert_sorted(9)
d.insert_sorted(4)
d.insert_sorted(6)
d.print_list()
print("====")
d.insert_sorted(8)
d.print_list()
print("====")
d.delete_first()
d.print_list()