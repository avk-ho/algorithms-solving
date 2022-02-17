# https://www.algoexpert.io/questions/Breadth-first%20Search

# First attempt

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = []
        queue.append(self)

        while len(queue) > 0:
            first_in_queue = queue[0]
            array.append(first_in_queue.name)
            if len(first_in_queue.children) > 0:
                for child in first_in_queue.children:
                    queue.append(child)
            queue.remove(first_in_queue)
        
        return array

# More clean solution

    def breadthFirstSearchSol(self, array):
        queue = [self]

        while len(queue) > 0:
                current = queue.pop(0)
                array.append(current.name)
                
                for child in current.children:
                    queue.append(child)

        return array

# O(V+E)T // O(V)S
# V being the number of vertices (nodes) and 
# E the number of edges (connections between nodes)