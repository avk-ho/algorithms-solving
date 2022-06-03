# https://www.algoexpert.io/questions/min-max-stack-construction

# First solution

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minmax = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]

    def pop(self):
        if len(self.stack) > 0:
            self.minmax.pop()
            return self.stack.pop()

    def push(self, number):
        if len(self.stack) == 0:
            newMinMax = {
                "min": number,
                "max": number
                }
        elif number > self.minmax[len(self.minmax) - 1]["max"]:
            newMinMax = {
                "min": self.minmax[len(self.minmax) - 1]["min"],
                "max": number
            }
        elif number < self.minmax[len(self.minmax) - 1]["min"]:
            newMinMax = {
                "min": number,
                "max": self.minmax[len(self.minmax) - 1]["max"]
            }
        else:
            newMinMax = self.minmax[len(self.minmax) - 1]
        self.stack.append(number)
        self.minmax.append(newMinMax)
        

    def getMin(self):
        if len(self.stack) > 0:
            return self.minmax[len(self.minmax) - 1]["min"]

    def getMax(self):
        if len(self.stack) > 0:
            return self.minmax[len(self.minmax) - 1]["max"]
