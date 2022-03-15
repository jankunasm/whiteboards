# Move Zeros
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example Input: [0,0,11,2,3,4]
# Example Output: [11,2,3,4,0,0]

def movezeros(alist):
    counter = 0
    while 0 in alist:
        alist.remove(0)
        counter += 1
    for inc in range(counter):
        alist.append(0)
    return alist

print(movezeros([0,0,11,2,3,4]))