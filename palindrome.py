"""
Check if the given number  (word) is a palindrome.

Args: number (int) or word (str): Variable to check.

Returns: bool: True if the number (word) is a palindrome, False otherwise.
"""

def palindrome_number(number):
    #Convert the number to a string, reverse it, convert it back to an integer,
    return True if int(str(number)[::-1])==number else False    

def palindrome_word(word):
    return True if word == word[::-1] else False

print(palindrome_number(12333456))
print(palindrome_word("Anna"))

