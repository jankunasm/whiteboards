# Count Palindromes
# GIven a list of strings, count the number of palindromes that occur inside of the list (a palindrome is a word that is spelled the same backwards and forward).

# Example input: ['dog', 'racecar', 'wildebeest']
# Output: 1
# Explanation: 'racecar' is the only palindrome in the list

def palindrone(someList):
    count = 0
    for word in someList:
        if word == word[::-1]:
            count += 1
    return count


print(palindrone(['dog', 'racecar', 'wildabeast']))