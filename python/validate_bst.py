# https://www.algoexpert.io/questions/Validate%20BST

# First attempt

# This is an input class. Do not edit.
import math

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, -math.inf, math.inf)

def validateBstHelper(tree, min, max):
    if tree is None:
        return True
    elif min > tree.value or tree.value >= max:
        return False

    return validateBstHelper(tree.left, min, tree.value) and validateBstHelper(tree.right, tree.value, max)