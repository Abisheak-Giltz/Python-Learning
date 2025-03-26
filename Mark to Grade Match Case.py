userInput = input("Enter your Mark : ")
mark = int(userInput)

match mark:
    case mark if 90 <= mark <= 100 :
        print(f"Your mark is {mark} and Your grade is 'A'")
    case mark if 80 <= mark <= 89 :
        print(f"Your mark is {mark} and Your grade is 'B'")
    case mark if 70 <= mark <= 79 :
        print(f"Your mark is {mark} and Your grade is 'C'")
    case mark if 60 <= mark <= 69 :
        print(f"Your mark is {mark} and Your grade is 'D'")
    case mark if 0 <= mark <= 59 :
        print(f"Your mark is {mark} and Your grade is 'F'. You Failed!")
    case _ :
        print(f"{mark} cannot be graded, give a valid mark!")
