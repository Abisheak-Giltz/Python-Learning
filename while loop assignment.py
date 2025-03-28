# While loop


# addition loop from 1 to 50
add = 0
count = 0

while count <= 50 :
    add += count
    count += 1

print(add)




# Count no. of digits in the given Input

word = input("Enter numbers to count digits: ")
digits = 0
i = 0

while i < len(word) :
    digits += 1
    i += 1
print(f"The length of the Digit is : {digits}")





# Factorial

userInput = input("Enter a Number to find its Factorial : ")
n = int(userInput)
factorial = 1
i = 1

while i <= n :
    factorial *= i
    i += 1
print(factorial)

