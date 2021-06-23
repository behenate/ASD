class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.is_right = None


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
                new.is_right = False
                root.left = new
        elif new.key > root.key:
            if root.right is not None:
                root = root.right
            else:
                new.parent = root
                new.is_right = True
                root.right = new

        else:
            print("Użyto istniejącego klucza!")
            return None


def find_next(node):
    if node.right is not None:
        return min_bst(node.right)
    if node.parent is None:
        return None
    while node.parent is not None:
        if node.is_right:
            return node.parent
        node = node.parent
    return node


def find_prev(node):
    if node.left is not None:
        max_bst(node.left)
    if node.paent is None:
        return None
    while node.parent is not None:
        if not node.is_right:
            return node.parent
        node = node.parent
    return node


def remove(node):
    # Jak jest ostanim w drzewie
    if node.left is None and node.right is None and node.parent is None:
        return None

    elif node.left is not None and node.right is None:
        if node.is_right:
            node.parent.right = node.left
        else:
            node.parent.left = node.left
        node.left.parent = node.parent
        node.left.is_right = node.is_right

    elif node.left is None and node.right is not None:
        if node.is_right:
            node.parent.right = node.right
        else:
            node.parent.left = node.right
        node.right.parent = node.parent
        node.right.is_right = node.is_right

    elif node.left is None and node.right is None:
        if node.is_right:
            node.parent.right = None
        else:
            node.parent.left = None
    else:
        to_link = find_next(node)
        node.key = to_link.key
        remove(to_link)
