# Max-Of-Three-Numbers

def maxNumber(x, y, z) :
    if (x > y) and (x > z) :
        return x
    elif (y > x) and (y > z) :
        return y
    elif (z > x) and (z > y) :
        return z

print(maxNumber(18, -2, -8))




# Print-Pattern

def printPattern(n) :
    for a in range(n) :
        for b in range(a + 1) :
            print("#", end = " ")
        print()


userInput = int(input("Enter a number : "))
printPattern(userInput)



# Check-Prime-Number

def checkPrime(num) :
    if num == 1 or num < 1:
        print(f"{num} is not a prime number.")
        return
    elif num >= 2 :
        for i in range(2, num) :
            if num % i == 0:
                print(f"The number {num} is not a prime number.")
                return
        print(f"The number {num} is a prime Number.")
            
    

userPrime = int(input("Enter a Number : "))
checkPrime(userPrime)
