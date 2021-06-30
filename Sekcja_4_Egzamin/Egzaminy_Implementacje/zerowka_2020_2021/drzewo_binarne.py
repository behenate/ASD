from zad2testy import runtests
from math import inf
class Node:
    def __init__(self, letter):
        self.letter = letter
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.j = None

def traverse(t, k):
    if t.left:
        traverse(t.left, k)
    t.j = [-inf for _ in range(k+1)]
    t.j[0] = 0
    if t.right:
        traverse(t.right, k)

def valuable_tree(T, k):
    def recur_calc(node, k):
        if node.j[k] != -inf:
            return node.j[k]
        if node.left and node.right:
            for t in range(k-1):
                vl = recur_calc(node.left, k-t-1) + node.leftval
                vr = recur_calc(node.right, t) + node.rightval
                node.j[k] = max(node.j[k], vr + vl)
                print(node.letter, node.j,k, vl, vr, k, t)
        vl = -inf
        vr = -inf
        if node.left:
            vl = recur_calc(node.left, k - 1) + node.leftval
            print(vl)
        if node.right:
            vr = recur_calc(node.right, k - 1) + node.rightval
            print(vr)
        print(vl, vr, node.j[k])
        node.j[k] = max(node.j[k], vl, vr)
        return node.j[k]
    maxi = -inf
    traverse(T,k)
    def traverse_calc(t):
        if t.left:
            traverse_calc(t.left)
        nonlocal maxi
        maxi = max(maxi, recur_calc(t, k))
        if t.right:
            traverse_calc(t.right)
    traverse_calc(T)
    print(maxi)
    return maxi


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
a.left = b
a.leftval = -1
a.right = e
a.rightval = -5
b.left = d
b.leftval = -6
b.right = c
b.rightval = -2
c.left = f
c.leftval = -8
c.right = g
c.rightval = -10


valuable_tree(a, 3)
# runtests(valuable_tree)