# https://www.algoexpert.io/questions/min-height-bst

# BST Class given with insert method
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

# First solution
def minHeightBst(array):

    def findMiddleOfArrayIndex(array):
        if len(array) % 2 == 0:
            return int(len(array)/2)
        else:
            return int((len(array)/2) - 0.5)

    def minHeightBstHelper(array, bst_node, bst_node_idx):
        if len(array) == 0:
            return
        else:
            # left side
            array_left = array[:bst_node_idx]
            if len(array_left) > 0:
                left_value_idx = findMiddleOfArrayIndex(array_left)
                new_left_node = array_left[left_value_idx]
                bst_node.insert(new_left_node)
                minHeightBstHelper(array_left, bst_node.left, left_value_idx)

            # right side
            array_right = array[bst_node_idx+1:]
            if len(array_right) > 0:
                right_value_idx = findMiddleOfArrayIndex(array_right)
                new_right_node = array_right[right_value_idx]
                bst_node.insert(new_right_node)
                minHeightBstHelper(array_right, bst_node.right, right_value_idx)


    if len(array) % 2 == 0:
        node_idx = int(len(array)/2)
        node_value = array[node_idx]
        bst = BST(node_value)
    else:
        node_idx = int((len(array)/2) - 0.5)
        node_value = array[node_idx]
        bst = BST(node_value)

    minHeightBstHelper(array, bst, node_idx)
    return bst

# (start_idx + end_idx) / 2, rounded up or down
# [0, 1, 2, 3, 4, 5, 6]
# [0, 1, 2, 3, 4]
# [0, 1, 2] 
# [0, 1]
# [0]

# Second solution
# using indices of array instead of slices
def minHeightBst(array):

    def findMiddleOfArrayIndex(start_idx, end_idx):
        if start_idx >= end_idx:
            return start_idx
        else:
            sum_idx = start_idx + end_idx
            if sum_idx % 2 == 0:
                return int(sum_idx / 2)
            else:
                return int((sum_idx / 2) - 0.5)

    def minHeightBstHelper(bst_node, node_idx, start_idx, end_idx):
        # left side
        if start_idx <= (node_idx - 1):
            left_node_idx = findMiddleOfArrayIndex(start_idx, node_idx - 1)
            bst_node.insert(array[left_node_idx])
            minHeightBstHelper(bst_node.left, left_node_idx, start_idx, node_idx - 1)

        # right side
        if (node_idx + 1) <= end_idx:
            right_node_idx = findMiddleOfArrayIndex(node_idx + 1, end_idx)
            bst_node.insert(array[right_node_idx])
            minHeightBstHelper(bst_node.right, right_node_idx, node_idx + 1, end_idx)


    node_idx = findMiddleOfArrayIndex(0, len(array) - 1)
    bst = BST(array[node_idx])

    minHeightBstHelper(bst, node_idx, 0, len(array) - 1)
    return bst

# [1, 2, 5]

# odd length array
# [0, 1, 2, 3, 4, 5, 6] start 0, end 6, middle 3
# [0, 1, 2] start 0, end 2, mid 1 | [4, 5, 6] start 4, end 6, mid 5
# [0] | [2] || [4] | [6]

# even length array
# [0, 1, 2, 3, 4, 5] start 0, end 5, middle 2
# [0, 1] start 0, end 1, middle 0 | [3, 4, 5] start 3, end 5, middle 4
# [1] || [3] | [5]

# Third solution
# similar to the second solution, but manually adding the left and right nodes
# improving time complexity
def minHeightBst(array):

    def findMiddleOfArrayIndex(start_idx, end_idx):
        if start_idx > end_idx:
            return None
        else:
            sum_idx = start_idx + end_idx
            return sum_idx // 2

    def minHeightBstHelper(bst_node, node_idx, start_idx, end_idx):
        # left side
        if start_idx <= (node_idx - 1):
            left_node_idx = findMiddleOfArrayIndex(start_idx, node_idx - 1)
            bst_node.left = BST(array[left_node_idx])
            minHeightBstHelper(bst_node.left, left_node_idx,
                               start_idx, node_idx - 1)

        # right side
        if (node_idx + 1) <= end_idx:
            right_node_idx = findMiddleOfArrayIndex(node_idx + 1, end_idx)
            bst_node.right = BST(array[right_node_idx])
            minHeightBstHelper(bst_node.right, right_node_idx,
                               node_idx + 1, end_idx)

    node_idx = findMiddleOfArrayIndex(0, len(array) - 1)
    bst = BST(array[node_idx])

    minHeightBstHelper(bst, node_idx, 0, len(array) - 1)
    return bst
