# Count Palindromes
# Given a list of strings, count the number of palindromes that occur 
# inside of the list (a palindrome is a word that is spelled the same backwards and forward).

# Example input: ['dog', 'racecar', 'wildebeest']
# Output: 1
# Explanation: 'racecar' is the only palindrome in the list

def count_pals(alist):
    counter = 0
    for word in alist:
        if word == word[::-1]:
            counter += 1
    return counter

print(count_pals(['dog', 'racecar', 'wildebeest']))