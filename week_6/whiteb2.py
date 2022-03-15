# Find Middle Number
# Given a number (n) and an array of numbers (num_list) as input to a function, return True if the number is greater than the middle number of the array. Return False if the number is less than the middle number of the array.
# Example Input: n = 6, array = [3,5,8, 10]
# Example Output: True
# Example Input: n = 105, array = [10,30,44,22,100]
# Example Output: True

list_a = [3, 5, 8, 10]
list_b = [10, 30, 44, 22, 100]

def compare_middle(n, num_list):
    if len(num_list) % 2 != 0:
        dynamic_index = len(num_list) // 2
    else:
        dynamic_index = (len(num_list) // 2) - 1
    if num_list[dynamic_index] < n:
        return True
    else:
        return False

print(compare_middle(45, list_b))