# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def squaredsum(array):
    newlist = []
    for i in array:
        newlist.append(i**2)
    return sum(newlist)

print(squaredsum([1, 2, 2]))