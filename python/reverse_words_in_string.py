# https://www.algoexpert.io/questions/Reverse%20Words%20In%20String

# cannot use built in .split, .reverse methods
# .join is ok

# First solution
def reverseWordsInString(string):
    stack = []
    i = 0
    word = ""
    while i < len(string):
        new_character = string[i]
        if len(word) == 0:
            word += new_character

        else:
            last_current_character = word[len(word)-1]

            # chain of empty spaces // could be combined with chain of characters
            if last_current_character == " " and new_character == " ":
                word += new_character
            # end of the chain of empty spaces // could be combined with end of chain of characters
            elif last_current_character == " " and new_character != " ":
                stack.append(word)
                word = new_character
            # chain of characters
            elif last_current_character != " " and new_character != " ":
                word += new_character
            # end of a chain of characters
            elif last_current_character != " " and new_character == " ":
                stack.append(word)
                word = new_character

        i += 1

    output = word
    while len(stack) > 0:
        new_chain = stack.pop()
        output += new_chain

    return output



# Slightly improving time complexity by avoiding 
# string concatenation as much as possible
def reverseWordsInString(string):
    stack = []
    i = 0
    word = []
    while i < len(string):
        new_character = string[i]
        if len(word) == 0:
            word.append(new_character)

        else:
            last_current_character = word[len(word)-1]

            # chain of empty spaces // could be combined with chain of characters
            if last_current_character == " " and new_character == " ":
                word.append(new_character)
            # end of the chain of empty spaces // could be combined with end of chain of characters
            elif last_current_character == " " and new_character != " ":
                stack.append(word)
                word = [new_character]
            # chain of characters
            elif last_current_character != " " and new_character != " ":
                word.append(new_character)
            # end of a chain of characters
            elif last_current_character != " " and new_character == " ":
                stack.append(word)
                word = [new_character]

        i += 1

    output = "".join(word)
    while len(stack) > 0:
        new_string = stack.pop()
        output += "".join(new_string)

    return output
