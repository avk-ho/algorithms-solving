# https://www.algoexpert.io/questions/Branch%20Sums

# First attempt

# This is the class of the input node. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = []

    exploreNode(root, result, 0)

    return result

def exploreNode(node, result, currentSum):
    currentSum += node.value

    current_left = node.left
    current_right = node.right

    if current_left is not None:
        exploreNode(node.left, result, currentSum)

    if current_right is not None:
        exploreNode(node.right, result, currentSum)

    if current_left is None and current_right is None:
        result.append(currentSum)

# O(N)ST
# N being the number of nodes
# We traverse each node once, and the length of the result array is 
# the number of leaves which would be roughly half the number of nodes in the worst case 
# (balanced binary tree)