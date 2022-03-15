def majelement(array):
    firstele = []
    secondele = []
    x = array[0]
    for i in array:
        if i == x:
            firstele.append(i)
        elif i != x:
            secondele.append(i)
    if len(firstele) > len(secondele):
        return firstele[0]
    elif len(firstele) == len(secondele):
        print('They is no winner!')
    else:
        return secondele[0]

print(majelement([2,2,1,1,1,2,1]))
    