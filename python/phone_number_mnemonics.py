# https://www.algoexpert.io/questions/Phone%20Number%20Mnemonics

# 0 / 1 / 2 abc / 3 def / 4 ghi / 5 jkl / 6 mno / 7 pqrs / 8 tuv / 9 wxyz
# phoneNumber is a string

# First attempt
def phoneNumberMnemonics(phoneNumber):


    def phoneNumberMnemonicsHelper(current_idx, code):
        for character in association_dict[phoneNumber[current_idx]]:
            new_code = code
            new_code += character
            if current_idx < len(phoneNumber) - 1:
                phoneNumberMnemonicsHelper(current_idx + 1, new_code)
            else:
                output.append(new_code)


    numbers = "0123456789"
    characters = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    association_dict = {key:value for (key, value) in zip(numbers, characters)}
    
    code = ""
    output = []

    phoneNumberMnemonicsHelper(0, code)

    return output

# 1905