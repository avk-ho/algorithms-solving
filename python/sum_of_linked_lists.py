# https://www.algoexpert.io/questions/sum-of-linked-lists

# First solution
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):

    def DivisionHelper(LLOneValue, LLTwoValue, outputValue):
        remainder = (LLOneValue + LLTwoValue + outputValue) % 10
        quotient = (LLOneValue + LLTwoValue + outputValue) // 10
        return (remainder, quotient)


    def sumOfLinkedListsHelper(linkedListOne, linkedListTwo, outputList):
        if linkedListOne is None and linkedListTwo is None:
            return

        elif linkedListOne is None:
            divisionResult = DivisionHelper(0, linkedListTwo.value, outputList.value)
            remainder = divisionResult[0]
            quotient = divisionResult[1]
            outputList.value = remainder
            if linkedListTwo.next is None and quotient == 0:
                return
            else:
                outputList.next = LinkedList(quotient)
                sumOfLinkedListsHelper(None, linkedListTwo.next, outputList.next)

        elif linkedListTwo is None:
            divisionResult = DivisionHelper(linkedListOne.value, 0, outputList.value)
            remainder = divisionResult[0]
            quotient = divisionResult[1]
            outputList.value = remainder
            if linkedListOne.next is None and quotient == 0:
                return
            else:
                outputList.next = LinkedList(quotient)
                sumOfLinkedListsHelper(linkedListOne.next, None, outputList.next)

        else:
            divisionResult = DivisionHelper(linkedListOne.value, linkedListTwo.value, outputList.value)
            remainder = divisionResult[0]
            quotient = divisionResult[1]
            outputList.value = remainder
            if linkedListOne.next is None and linkedListTwo.next is None and quotient == 0:
                return
            else:
                outputList.next = LinkedList(quotient)
                sumOfLinkedListsHelper(linkedListOne.next, linkedListTwo.next, outputList.next)


    outputList = LinkedList(0)
    sumOfLinkedListsHelper(linkedListOne, linkedListTwo, outputList)

    return outputList

# A lot of redondant code

# Given solution (cleaner)
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedListHeadPointer = LinkedList(0)
    currentNode = newLinkedListHeadPointer
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumOfValues = valueOne + valueTwo + carry

        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currentNode.next = newNode
        currentNode = newNode

        carry = sumOfValues // 10
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return newLinkedListHeadPointer.next