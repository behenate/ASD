from queue import Queue
from print_tree import print_tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        if root.key < key:
            root = root.right
        else:
            root = root.left
    return None


def min_bst(root):
    while root.left is not None:
        root = root.left
    return root


def max_bst(root):
    while root.right is not None:
        root = root.right
    return root


def insert(root, new):
    while root is not None:
        if new.key < root.key:
            if root.left is not None:
                root = root.left
            else:
                new.parent = root
                root.left = new
                root = None
        elif new.key > root.key:
            if root.right is not None:
                root = root.right
            else:
                new.parent = root
                root.right = new
                root = None
        elif root.key == new.key:
            print("Użyto istniejącego klucza!")
            return None


def find_next(node):
    if node.right is not None:
        return min_bst(node.right)
    if node.parent is None:
        return None
    while node.parent is not None:
        if node.key > node.parent.key:
            return node.parent
        node = node.parent
    return node


def find_prev(node):
    if node.left is not None:
        max_bst(node.left)
    if node.paent is None:
        return None
    while node.parent is not None:
        if not node.key > node.parent.key:
            return node.parent
        node = node.parent
    return node


def remove(node):
    # Jak jest ostanim w drzewie
    if node.left is None and node.right is None and node.parent is None:
        return None

    elif node.left is not None and node.right is None:
        if node.key > node.parent.key:
            node.parent.right = node.left
        else:
            node.parent.left = node.left
        node.left.parent = node.parent

    elif node.left is None and node.right is not None:
        if node.key > node.parent.key:
            node.parent.right = node.right
        else:
            node.parent.left = node.right
        node.right.parent = node.parent

    elif node.left is None and node.right is None:
        if node.key > node.parent.key:
            node.parent.right = None
        else:
            node.parent.left = None
    else:
        to_link = find_next(node)
        if to_link.key > to_link.parent.key:
            to_link.parent.right = None
        else:
            to_link.parent.left = None
        node.key = to_link.key

def check(node, a, b):
    stack = []
    found = [0 for i in range(b-a+1)]
    cnt = 0
    while True:
        cnt += 1
        if node is None and len(stack) == 0:
            break
        if node and node.key > a:
            if node.key <=b:
                stack.append(node)
            node = node.left
        elif node and node.key <= a:
            stack.append(node)
            node = None
        elif node is None:
            node = stack.pop()
            if a <= node.key <= b:
                found[node.key-a] = 1
            if node.key <= b:
                node = node.right
            else:
                node = None
    for i in range(len(found)):
        if not found[i]:
            return False
    return True
tree = Node(12)
insert(tree, Node(9))
insert(tree, Node(13))
insert(tree, Node(8))
insert(tree, Node(15))
insert(tree, Node(6))
insert(tree, Node(14))
insert(tree, Node(7))
print_tree(tree)
print(check(tree, 6,9))