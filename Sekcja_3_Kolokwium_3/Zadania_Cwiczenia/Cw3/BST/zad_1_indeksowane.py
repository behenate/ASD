from print_tree import print_tree


class Node:
    def __init__(self, key, cnt):
        self.key = key
        self.cnt = cnt
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


def insert_bst(root, new):
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


def find_nth(node, n):
    if n == 1 and node.left is None:
        return node
    if n == node.left.cnt + 1:
        return node
    elif node.left is not None and n <= node.left.cnt:
        return find_nth(node.left, n)
    elif node.right is not None and n > node.right.cnt:
        return find_nth(node.right, n - (node.cnt - node.right.cnt))
    else:
        print("Ni ma")

def get_num(node, cnt = 0, add=True):
    left = 0
    if node.left is not None:
        left = node.left.cnt
    if add is True:
        cnt += left+1
    if node.parent is None:
        return cnt
    if node.parent.key < node.key:
        return get_num(node.parent, cnt, True)
    else:
        return get_num(node.parent, cnt, False)

tree = Node(20, 11)
insert_bst(tree, Node(15, 7))
insert_bst(tree, Node(40, 3))
insert_bst(tree, Node(11, 4))
insert_bst(tree, Node(18, 2))
insert_bst(tree, Node(39, 1))
insert_bst(tree, Node(41, 1))
insert_bst(tree, Node(8, 1))
insert_bst(tree, Node(12, 2))
insert_bst(tree, Node(16, 1))
insert_bst(tree, Node(13, 1))

print_tree(tree)
# print(find_nth(tree, 1).key)
print(get_num(find(tree, 18)), "co")