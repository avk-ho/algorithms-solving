# https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor

# First solution
def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    encrypted_str = ""
    for letter in string:
        letter_index = alphabet.index(letter)
        new_index = (letter_index + key) % 26
        encrypted_str += alphabet[new_index]
    
    return encrypted_str

# Second solution
def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    string = list(string)
    for i in range(len(string)):
        current_index = alphabet.index(string[i])
        new_index = (current_index + key) % 26
        string[i] = alphabet[new_index]
    string = "".join(string)
    return string