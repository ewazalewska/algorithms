# Algorithm counts the occurrences of each character in the given string

sentence = "Python is the best!"

occurrences = {}

for mark in sentence:
    if mark not in occurrences.keys():      # Check if the character is a key in the dictionary
        occurrences[mark] = 1               # If not, add it to the dictionary with a count of 1
    else:
        occurrences[mark] += 1              # If already a key, increment the count by 1

print(occurrences)