# https://www.algoexpert.io/questions/BST%20Construction

# First attempt
# Adding properties and methods is allowed
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BST(value)
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value and self.left is not None:
            return self.left.contains(value)
        elif value > self.value and self.right is not None:
            return self.right.contains(value)
        else:
            return False

    def remove(self, value):
        # Do not edit the return statement of this method.
        if self.contains(value):
            # Single node tree case
            if self.left is None and self.right is None:
                return self

            # Finding the node of value and its parent
            if self.value == value:  # Value is the root node
                value_node = self
            else:
                value_parent = self.findParentOfValue(value)
                if value_parent.left.value == value:
                    value_node = value_parent.left
                else:
                    value_node = value_parent.right

            # Finding the replacement node, right child present
            if value_node.right is not None:
                replacement_node = value_node.right
                while replacement_node.left is not None:
                    replacement_node = replacement_node.left


                # Removal of the replacement node and fixing the tree if necessary
                replacement_parent = self.findParentOfValue(replacement_node.value)
                print(replacement_parent)
                if replacement_node.right is not None:
                    replacement_parent.left = replacement_node.right
                else:
                    replacement_parent.left = None

            # Finding the replacement node, left child only
            elif value_node.left is not None:
                replacement_node = value_node.left
                while replacement_node.right is not None:
                    replacement_node = replacement_node.right
          
                
                # Removal of the replacement node and fixing the tree if necessary
                replacement_parent = self.findParentOfValue(
                    replacement_node.value)
                print(replacement_parent)
                if replacement_node.left is not None:
                    replacement_parent.right = replacement_node.left
                else:
                    replacement_parent.right = None

            # The value node is a leaf node, removing the leaf
            else:
                if value_node == value_parent.left:
                    value_parent.left = None
                else:
                    value_parent.right = None

            # Swapping the value of the value node with its new value
            # replacement_value = replacement_node.value
            value_node.value = replacement_node.value

        return self

    def findParentOfValue(self, value):
        # Returns the parent node of value, to use after a contains() check
        if value < self.value:
            if self.left.value == value:
                return self
            else:
                return self.left.findParentOfValue(value)
        elif value > self.value:
            if self.right.value == value:
                return self
            else:
                return self.right.findParentOfValue(value)


# |             10
# |       5             14
# |    3     7      12      18
# |  2   4  6  8  11  13  15  20

# Invalid unbound local variable error
# Nonetype error