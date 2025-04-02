
userInput1 = int(input("Enter some numbers : "))
userInput2 = int(input("Enter some numbers : "))
userInput3 = int(input("Enter some numbers : "))

def dataAnalyzer(x, y, z) :
    numberList = [] # To store the input values to use min(), max(), sorted() default functions
    numberList.append(x)
    numberList.append(y)
    numberList.append(z)

    average = round(((x + y + z) / 3), 2)
    
    aboveAverage = 0 # To count the no. of values above average
    if(x > average) :
        aboveAverage += 1
    elif(y > average) :
        aboveAverage += 1
    elif(z > average) :
        aboveAverage += 1
    
    # The sum of all values
    print(f"The Sum of the given Numbers is {x + y + z}")
    
    # The minimum of all values
    print(f"The Minimum of the given Numbers is {min(numberList)}")

    # The maximum of all values
    print(f"The Maximum of the given Numbers is {max(numberList)}")

    # The average of all values
    print(f"The Average of the given Numbers is {average}")

    # The number of values that are above average
    print(f"The Number of values that is above average is {aboveAverage}")

    # The sorted list of the values
    print(f"The Sorted list is {sorted(numberList)}")



dataAnalyzer(userInput1, userInput2, userInput3)
