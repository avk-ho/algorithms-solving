# https://www.algoexpert.io/questions/invert-binary-tree

# First solution

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
    if tree is not None:
        tree.left, tree.right = tree.right, tree.left
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
    