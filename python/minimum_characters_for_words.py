# https://www.algoexpert.io/questions/Minimum%20Characters%20For%20Words

# Ex : output ["y", "o", "u", "r"] for input ["your", "you", "or", "yo"]
# no spaces in the input, but special characters may appear
# if multiples "same" characters are needed for a single word, 
# they need to be added multiple times in the output

# First attempt
def minimumCharactersForWords(words):
    letters_dict = {}
    
    # Looping through all words
    for word in words:
        letters_temp = {}

        # Looping through all letters in a word, counting the number of each character
        for letter in word:
            if letter in letters_temp:
                letters_temp[letter] += 1
            else:
                letters_temp[letter] = 1
        
        # Looping through the resulting dict and comparing to the pre output one
        for letter in letters_temp:
            if letter in letters_dict:
                if letters_temp[letter] > letters_dict[letter]:
                    letters_dict[letter] = letters_temp[letter]
            else:
                letters_dict[letter] = letters_temp[letter]

    # Looping through the pre output dict to generate the output
    output = []
    for letter in letters_dict:
        for n in range(letters_dict[letter]):
            output.append(letter)

    return output

# Extremely poor time complexity, having multiple nested loops followed by another loop