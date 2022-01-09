# https://www.algoexpert.io/questions/Run-Length%20Encoding

# First solution
def runLengthEncoding(string):
    input = list(string)
    output = ""
    current_character = ""
    counter = 0
    for i in range(len(input)):
        if current_character == "":
            current_character = input[i]
        if current_character == input[i]:
            counter += 1
            if counter > 9:
                output += "9" + current_character
                counter = 1
        else:
            output += str(counter) + current_character
            current_character = input[i]
            counter = 1
        if i == len(input)-1:
            output += str(counter) + current_character
    
    return output

# Second solution
def runLengthEncoding(string):
    input = list(string)
    output = ""
    current_character = ""
    counter = 0
    for i in range(len(input)):
        if current_character == "":
            current_character = input[i]
        if counter == 9 or current_character != input[i]:
            output += str(counter) + current_character
            current_character = input[i]
            counter = 1
        else:
            counter += 1
        if i == len(input)-1:
            output += str(counter) + current_character
    
    return output

# Third solution
# Switched the output from a string to a list
def runLengthEncoding(string):
    input = list(string)
    output = []
    current_character = ""
    counter = 0
    for i in range(len(input)):
        if current_character == "":
            current_character = input[i]
        if counter == 9 or current_character != input[i]:
            output.append(str(counter))
            output.append(current_character)
            current_character = input[i]
            counter = 1
        else:
            counter += 1
        if i == len(input)-1:
            output.append(str(counter))
            output.append(current_character)
    
    return "".join(output)
