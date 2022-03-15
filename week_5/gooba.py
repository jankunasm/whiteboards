# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def num(array):
    new_list = []
    for i in array:
        if i > 0:
            new_list.append(i)
        if new_list == []:
            return 0
    return sum(new_list)
print (num([1,-4,7,12]))