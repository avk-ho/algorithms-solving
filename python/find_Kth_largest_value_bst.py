# https://www.algoexpert.io/questions/find-kth-largest-value-in-bst

# First solution
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):

    def reverseInOrderTraverse(tree, array):
        if tree is None:
            return
        else:
            reverseInOrderTraverse(tree.right, array)
            array.append(tree.value)
            reverseInOrderTraverse(tree.left, array)
            
        return array

    largestValueArray = reverseInOrderTraverse(tree, [])
    return largestValueArray[k-1]