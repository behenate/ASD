class Node:
    def __init__(self):
        self.children = 2
        self.child = []
        self.g = -1
        self.f1 = -1
        self.f2 = -1

    def calc_f(self):
        if self.f1 != -1:
            return self.f1
        if len(self.child) == 0:
            self.f1 = 0
            return 0

        for c in self.child:
            child_f = c[0].calc_f()
            if child_f + c[1] > self.f1:
                self.f2 = self.f1
                self.f1 = child_f + c[1]
            elif child_f + c[1] > self.f2:
                self.f2 = child_f + c[1]
        return self.f1

    def calc_g(self):
        if self.g != -1:
            return self.g
        if self.f1 > 0:
            self.g = self.f1
        else:
            self.g = 0
        if self.f2 > 0:
            self.g += self.f2
        return self.g


A = Node()
B = Node()
C = Node()
A.children = 2
A.child = [(B, 5), (C, -1)]
A.calc_f()
A.calc_g()
print(A.g, A.f1, A.f2)
