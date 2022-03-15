# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

# If the input array is empty or null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def arraymanip(array):
    first_list = []
    second_list = []
    for i in array:
        if i >= 0:
            first_list.append(i)
        elif i < 0:
            second_list.append(i)

    print(len(first_list))
    print(sum(second_list))
    

print(arraymanip([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))