class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    # Próba połączenia dwóch elementów z tego samego zbioru
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

union(a,b)
print(a.parent.val)
union(c,d)
print(c.parent.val)
union(a,d)
print(c.parent.val)
union(a,e)
print(e.parent.val)
