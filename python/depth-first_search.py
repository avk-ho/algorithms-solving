# https://www.algoexpert.io/questions/Depth-first%20Search

# First attempt

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)

        for child in self.children:
            child.depthFirstSearch(array)

        return array

# O(V+E)T // O(V)S
# V being the number of vertices (nodes) and
# E being the number of edges (connections between nodes)