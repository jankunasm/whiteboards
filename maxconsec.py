# Max consecutive Nums:

# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Input: nums = [1,1,1,0,1,1,1,0]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. 
# The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

def binary_count(nums):
    counter = 0
    max_count = 0
    for number in nums:
        if number == 1:
            counter += 1
            if counter > max_count:
                max_count = counter
        else:
            counter = 0
    return max_count

print(binary_count([1,0,1,0,1,0,1,1,0,0,0]))