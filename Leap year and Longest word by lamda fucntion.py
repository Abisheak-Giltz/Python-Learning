
# Leap Year

userInput = int(input("Enter a year : "))
isLeapYear = lambda x : f"{x} a leap year" if (x % 4 == 0) else f"{x} is not a leap year"

print(isLeapYear(userInput))

# Longest word

from functools import reduce

a = ["python", "java", "javascript", "sql", "c"]
longestWord = reduce((lambda x, y : x if len(x) > len(y) else y), a)


print(longestWord)
