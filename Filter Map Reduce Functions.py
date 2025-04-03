
array = [-46, 5, 10, 15, -20, -8, 30]

def transformData(x) :
    if (x < 0) :
        return False
    else:
        return True


removeNegativeNumbers = filter(transformData, array)
print(removeNegativeNumbers)
