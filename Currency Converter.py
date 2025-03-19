#currency conversion

userInput = input("Enter value in INR: ")
moneyValue = int(userInput)

userChoice = input("Enter a valid currency code: ")
moneyToChangeTo = userChoice.lower()


if moneyToChangeTo == "yen":
    print(f"¥{moneyValue * 1.74} {userChoice}")
elif moneyToChangeTo == "dollar":
    print(f"${moneyValue * 0.012} {userChoice}")
elif moneyToChangeTo == "riyal":
    print(f"﷼{moneyValue * 0.043} {userChoice}")
elif moneyToChangeTo == "euro":
    print(f"€{moneyValue * 0.011} {userChoice}")
elif moneyToChangeTo == "pound":
    print(f"£{moneyValue * 0.0089} {userChoice}")
