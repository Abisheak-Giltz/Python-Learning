name = input("Enter Your Name: ")
firstName = name.split(" ")[0]
secondName = name.split(" ")[1]

print(f"Your first name is {firstName}\nYour second name is {secondName}")


currentYear = input("Enter current year: ")
birthYear = input("Enter your Birth year: ")
age = int(currentYear) - int(birthYear)
print(f"Your current age is {age}")
