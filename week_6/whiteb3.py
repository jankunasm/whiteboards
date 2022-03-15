# Title Case
# ----------
# A string is considered to be in title case if each word in the string 
# is either (a) capitalized or (b) considered to be an exception and put 
# entirely into lower case unless it is the first word, which is always 
# capitalized.
# Write a function that will convert a string into title case, given an 
# optional list of exceptions (minor words). The list of minor words will 
# be given as a string with each word separated by a space. Your function 
# should ignore the case of the minor words string -- it should behave in 
# the same way even if the case of the minor word string is changed.

# Example 1
# Input: title_case('POWER RANGERS in space', 'in')

# Output: 'Power Rangers in Space'

# Example 2

# Input: title_case('the death of a bachelor', 'the, of, a')

# Output: The Death of a Bachelor

def caps_list(string1, string2):
    x = string1.split(' ')
    y = string2.split(' ')
    for i in range(len(x)):
        if i == 0:
            x[i] = x[i].title()
        elif x[i] in y:
            continue
        else:
            x[i] = x[i].title()
    return " ".join(x)
    
print(caps_list('POWER RANGERS in space', 'in'))

