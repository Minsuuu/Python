class MyArray:
    def __init__(self):
        self.s = []

    def add(self, k):
        self.s += [0]
        pos = 0

        if len(self.s) > 0:
            for i in range(0, len(self.s)):
                if self.s[i] > k:
                    break

            pos = i

    for i in range(len(self.s) - 1, pos, -1):
        self.s[i] = self.s[i - 1]

    self.s[pos] = k

    def delete(self, k):
        pos = -1
        for i in range(len(self.s)):
            if k == self.s[i]:
                pos = i
                break
        if pos == -1:
            return
        else:
            for i in range(pos, len(self.s) - 1):
                self.s[i] = self.s[i + 1]
                self.s.pop()

    def search(self, k):
        low, high = 0, len(self.s) - 1
        m = 0

        while low < high:
            m = (low + high) // 2
            if self.s[m] == k:
                return m
            elif self.s[m] > k:
                high = m - 1
            else:
                low = m + 1
    def print_all(self):
        print(self.s)

x = MyArray()
x.add(8)
x.add(2)
x.add(3)
x.print_all()
x.add(33)
x.print_all()
x.add(40)
x.print_all()

p = x.search(33)
print(p)
p = x.search(8)
print(p)

x.delete(5)
x.print_all()
x.delete(2)
x.print_all()
x.delete(40)
x.print_all()