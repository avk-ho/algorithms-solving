# https://www.algoexpert.io/questions/bst-traversal

# First solution

# should return a sorted array of the BST's nodes values
def inOrderTraverse(tree, array):
    if tree is not None:
        return
    else:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)

    return array

# going from a node then its left, then its right
def preOrderTraverse(tree, array):
    if tree is None:
        return
    else:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)

    return array

# "climbing back" from the farthest nodes, starting from the left side
def postOrderTraverse(tree, array):
    if tree is None:
        return
    else:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)

    return array

#