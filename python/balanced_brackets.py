# https://www.algoexpert.io/questions/Balanced%20Brackets

# First attempt
def balancedBrackets(string):
    bracket_pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    open_brackets = ["(", "{", "["]

    stack = []
    for character in string:
        # if the character is a closing bracket
        if character in bracket_pairs:
            # if there is no opening bracket
            if len(stack) == 0:
                return False
            else:
                last_open_bracket = stack.pop()
                print(last_open_bracket + character)
                # checking if the closing bracket correspond to the last opening bracket
                if last_open_bracket != bracket_pairs[character]:
                    return False
                print(stack)
        else:
            if character in open_brackets:
                stack.append(character)

            print(stack)
    
    if len(stack) != 0:
        return False

    return True

# Clean version
def balancedBrackets(string):
    bracket_pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    open_brackets = ["(", "{", "["]

    stack = []
    for character in string:
        if character in bracket_pairs:
            if len(stack) == 0:
                return False
            else:
                last_open_bracket = stack.pop()
                if last_open_bracket != bracket_pairs[character]:
                    return False
        else:
            if character in open_brackets:
                stack.append(character)

    if len(stack) != 0:
        return False

    return True

# Space time complexity O(n)ST with n the length of the string