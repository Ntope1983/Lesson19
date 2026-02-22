from typing import Any


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        n = Node(data)
        self.root = n

    def insert_left(self, node, data):
        n = Node(data)
        node.left = n

    def insert_right(self, node, data):
        n = Node(data)
        node.right = n

    def __str__(self):
        st = ""

        def rec_str(n):
            nonlocal st

            if n is None:
                st += "_"
            else:
                st += str(n.data)
                st += "("
                rec_str(n.left)
                st += ","
                rec_str(n.right)
                st += ")"

        rec_str(self.root)
        return st


class BinarySearchTree(Tree):
    def insert(self, insert_data):

        def insert_subtree(node, data):
            if data < node.data and node.left is not None:
                insert_subtree(node.left, data)

            elif data > node.data and node.right is not None:
                insert_subtree(node.right, data)

            elif data < node.data and node.left is None:
                self.insert_left(node, data)

            elif data > node.data and node.right is None:
                self.insert_right(node, data)

        if self.root is None:
            self.insert_root(insert_data)
        else:
            insert_subtree(self.root, insert_data)

    def inorder(self):
        result = []
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            result.append(node.data)
            traverse(node.right)
        traverse(self.root)
        return result


x = BinarySearchTree()
x = BinarySearchTree()
x.insert(50)
x.insert(30)
x.insert(70)
x.insert(20)
x.insert(40)
x.insert(35)
y = x.inorder()
for item in y:
    print(item)
