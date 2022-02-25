# https://www.algoexpert.io/questions/Node%20Depths

# The root node is depth 0

# First attempt
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root):
    depth = 0
    return nodeDepthsHelper(root, depth)


def nodeDepthsHelper(node, depth_lvl):
    new_depth = depth_lvl + 1
    if node.left is not None and node.right is not None:
        return depth_lvl + nodeDepthsHelper(node.left, new_depth) + nodeDepthsHelper(node.right, new_depth)
    elif node.left is not None:
        return depth_lvl + nodeDepthsHelper(node.left, new_depth)
    elif node.right is not None:
        return depth_lvl + nodeDepthsHelper(node.right, new_depth)
    else:
        return depth_lvl

# Recursive solution


# Second attempt
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

# Simplified version, if modification of the parameters is allowed