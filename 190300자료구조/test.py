def bin2dec(s):
    length = len(s)
    result = 0
    for i in range(length-1, -1, -1):
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