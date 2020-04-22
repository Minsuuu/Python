class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
    # 넣기 - 콘솔에서 호출할 때 사용하는 함수
    def put(self, key):
        self.root = self.put_item(self.root, key)
    # 넣기 - recursive 함수 사용
    def put_item(self, n, key):
        if n == None:
            return Node(key)
        elif key < n.key:
            n.left = self.put_item(n.left, key)
            return n
        elif key > n.key:
            n.right = self.put_item(n.right, key)
            return n
    # 찾기 - 콘솔에서 호출할 때 사용하는 함수
    def get(self, k):
        return self.get_key(self.root, k)
    # 찾기 - recursive 함수 사용
    def get_key(self, n, key):
        if n == None:
            return None
        elif key < n.key:
            return self.get_key(n.left, key)
        elif key > n.key:
            return self.get_key(n.right, key)
        else:
            return n.key
    # 빼기 - 콘솔에서 호출할 때 사용하는 함수
    def delete(self, k):
        self.root = self.delete_node(self.root, k)
    # 빼기 - recursive 함수 사용
    def delete_node(self, n, key):
        if n == None:
            return None
        elif key < n.key:
            n.left = self.delete_node(n.left, key)
            return n
        elif key > n.key:
            n.right = self.delete_node(n.right, key)
            return n
        else:
            if n.left == None:
                return n.right
            elif n.right == None:
                return n.left
            else:
                new_n = self.minimum(n.right)
                new_n.right = self.delete_min(n.right)
                new_n.left = n.left
                return new_n
    # subtree의 root 노드가 n일 때 최솟값 노드 찾기
    def minimum(self, n):
        if n.left == None:
            return n
        else:
            return self.minimum(n.left)
    # subtree의 root 노드가 n일 때 최솟값 노드 삭제하기
    def delete_min(self, n):
        if n.left == None:
            return n.right
        else:
            n.left = self.delete_min(n.left)
            return n
    # inorder traversal - 콘솔에서 호출할 때 사용하는 함수
    def inorder_print(self):
        self.inorder(self.root)
    # inorder traversal - recursive 함수
    def inorder(self, n):
        if n != None:
            self.inorder(n.left)
            print(n.key)
            self.inorder(n.right)
    # preorder traversal - 콘솔에서 호출할 때 사용하는 함수
    def preorder_print(self):
        self.preorder(self.root)
    # preorder traversal - recursive 함수
    def preorder(self, n):
        if n != None:
            print(n.key)
            self.preorder(n.left)
            self.preorder(n.right)
    # postorder traversal - 콘솔에서 호출할 때 사용하는 함수
    def postorder_print(self):
        self.postorder(self.root)
    # postorder traversal - recursive 함수
    def postorder(self, n):
        if n != None:
            self.postorder(n.left)
            self.postorder(n.right)
            print(n.key)
# 콘솔 코드 - 테스트용
t = BST()
t.put(1)
t.put(5)
t.put(4)
t.put(9)
t.put(10)
t.put(8)
t.inorder_print()
t.delete(5)
t.inorder_print()