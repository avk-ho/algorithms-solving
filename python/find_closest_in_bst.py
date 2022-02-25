# https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST

# a node value is always greater than all values to its left
# and greater or equal to all values to its right

# First attempt
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
    if tree.value == target:
        return tree.value
    else:
        closest = None
        current_tree = tree
        while current_tree is not None:
            if current_tree.value == target:
                return current_tree.value
            elif current_tree.value > target:
                if current_tree.left is not None:
                    if abs(target - current_tree.value) < abs(target - current_tree.left.value):
                        if closest is None or abs(target - closest) > abs(target - current_tree.value):
                            closest = current_tree.value
                    else:
                        if closest is None or abs(target - closest) > abs(target - current_tree.left.value):
                            closest = current_tree.left.value
                    current_tree = current_tree.left
                    print(f"closest : {closest}")
                else:
                    return closest
            else:
                if current_tree.right is not None:
                    if abs(target - current_tree.value) < abs(target - current_tree.right.value):
                        if closest is None or abs(target - closest) > abs(target - current_tree.value):
                            closest = current_tree.value
                    else:
                        if closest is None or abs(target - closest) > abs(target - current_tree.right.value):
                            closest = current_tree.right.value
                    current_tree = current_tree.right
                    print(f"closest : {closest}")
                else:
                    return closest

        return closest

# Fonctionnal, could be simplified

# Second solution
def findClosestValueInBst(tree, target):
    closest = tree.value
    current_tree = tree
    while closest != target:
        if abs(target - closest) > abs(target - current_tree.value):
            closest = current_tree.value

        if current_tree.value > target:
            if current_tree.left is None:
                return closest
            current_tree = current_tree.left
            print(f"closest : {closest}")
        else:
            if current_tree.right is None:
                return closest
            current_tree = current_tree.right
            print(f"closest : {closest}")

    return closest
