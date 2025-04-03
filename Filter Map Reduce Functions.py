
# Default functions Map(), Filter() & Reduce()

def filterData(x) :
    if(x >= 0) :
        return x



myList = [12, -1, -4, 16, -5, -56, -13, 7, 61, 36, 5]
filteredNegativeValues = list(filter(filterData, myList))
print(filteredNegativeValues)


def mapData(x) :
    return x * 2


squaredValues = list(map(mapData, myList))
print(squaredValues)



from functools import reduce

def reduceProduct(x, y) :
    return x + y

reducedProduct = reduce(reduceProduct, squaredValues)
print(reducedProduct)
