class Node:
    def __init__(self, parent=None, left=None, right=None, w_left=0, w_right=0):
        self.parent = parent
        self.left = left
        self.right = right
        self.w_left = w_left
        self.w_right = w_right
        self.g = None
        self.h = None
        self.f = None

    def gf(self):
        if self.g is not None:
            return self.g
        if self.left is None:
            self.g = 0
            return self.g
        c_g = self.left.gf()
        c_h = self.left.hf()
        self.g = max(self.w_left, self.w_left + max(c_g, c_h), 0)
        return self.g

    def hf(self):
        if self.h is not None:
            return self.h
        if self.right is None:
            self.h = 0
            return self.h
        c_g = self.right.gf()
        c_h = self.right.hf()
        self.h = max(self.w_right, self.w_right + max(c_g, c_h), 0)
        return self.h

    def ff(self):
        return max(0, self.hf()) + max(0, self.gf())


a = Node()
b = Node(parent=a)
c = Node(parent=a)
d = Node(parent=b)
e = Node(parent=b)
f = Node(parent=c)
g = Node(parent=f)
h = Node(parent=f)
a.left = b
a.w_left = 5
a.right = c
a.w_right = 4
b.left = d
b.w_left = 2
b.right = e
b.w_right = 3
c.right = f
c.w_right = -1
f.left = g
f.w_left = -2
f.right = h
f.w_right = 6


print(a.ff())

# Przejść po drzewie, wypisać max

