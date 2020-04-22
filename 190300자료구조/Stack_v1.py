class Stack:
    class Node:
        def __init__(self, data, link):
            self.data = data
            self.next = link

    def __init__(self):
        self.top = None

    def push(self, data):
        node = self.Node(data, self.top)
        self.top = node

    def pop(self):
        if self.top == None:
            return
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def peek(self):
        if self.top == None:
            return
        else:
            return self.top.data


def palindrome(s):
    stack = Stack()
    length = len(s)

    if (length % 2) == 0:
        for i in range(0, length // 2, 1):
            stack.push(s[i])
        for i in range(length // 2, length, 1):
            if s[i] == stack.pop():
                continue
            else:
                return False
        return True
    else:
        for i in range(0, length // 2, 1):
            stack.push(s[i])
        for i in range(length // 2 + 1, length, 1):
            if s[i] == stack.pop():
                continue
            else:
                return False
        return True


def calc_postfix(p):
    stack = Stack()
    result = 0

    for i in range(0, len(p), 1):
        if (p[i] == "+") or (p[i] == "-") or (p[i] == "*") or (p[i] == "/"):
            if p[i] == "+":
                result = stack.pop() + stack.pop()
                stack.push(result)
            elif p[i] == "-":
                temp = stack.pop()
                result = stack.pop() - temp
                stack.push(result)
            if p[i] == "*":
                result = stack.pop() * stack.pop()
                stack.push(result)
            elif p[i] == "/":
                temp = stack.pop()
                result = stack.pop() / temp
                stack.push(result)
        else:
            stack.push(int(p[i]))
    return stack.peek()


x = "3+4*5"
post = "345*+"
print(calc_postfix(post))