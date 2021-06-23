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


def tree_to_sorted(node):
    to_ret = []
    if node.left is not None:
        to_ret = tree_to_sorted(node.left)
    to_ret += [node.key]
    if node.right is not None:
        to_ret += tree_to_sorted(node.right)
    return to_ret


def find_common(tree1, tree2):
    t1 = tree_to_sorted(tree1)
    t2 = tree_to_sorted(tree2)
    common = []
    i = 0
    j = 0
    while i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            i += 1
        elif t1[i] > t2[j]:
            j += 1
        else:
            common.append(t1[i])
            i += 1
            j += 1
    new = Node(common[0])
    for i in range(1, len(common)):
        insert_bst(new, Node(common[i]))
    return new


tree = Node(20)
insert_bst(tree, Node(15))
insert_bst(tree, Node(40))
insert_bst(tree, Node(11))
insert_bst(tree, Node(18))
insert_bst(tree, Node(39))
insert_bst(tree, Node(41))
insert_bst(tree, Node(8))
insert_bst(tree, Node(12))
insert_bst(tree, Node(16))
insert_bst(tree, Node(13))

tree2 = Node(20)
insert_bst(tree2, Node(12))
insert_bst(tree2, Node(40))
insert_bst(tree2, Node(13))
insert_bst(tree2, Node(14))
insert_bst(tree2, Node(1))
insert_bst(tree2, Node(41))
insert_bst(tree2, Node(8))
insert_bst(tree2, Node(12))
insert_bst(tree2, Node(36))
insert_bst(tree2, Node(13))


tt = find_common(tree, tree2)

print_tree(tt)

