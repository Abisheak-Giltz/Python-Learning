# Find Common Elements

newList = []
def commonElements(list1, list2) :
    
    for i in list1 :
        for j in list2 :
            if (i == j) :
                newList.append(i)

commonElements([1, 2, 3, 4, 8], [2, 4, 6, 8])
print(newList)
