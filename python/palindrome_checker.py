# https://www.algoexpert.io/questions/Palindrome%20Check

# first solution

def isPalindrome(string):
	if type(string) != str:
		return "Error, wrong type imput"

	string = string.strip()
	string = list(string)
	string_copy = string.copy()
	string_copy.reverse()
	return string == string_copy

# solution 2

if str(string) == "".join(reversed(string)):
	return True
	else:
		return False