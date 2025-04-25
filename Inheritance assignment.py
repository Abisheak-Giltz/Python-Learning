
# Inheritance Assignment



class book:
    def details(self):
        print("This is a Book\n")

class textBook(book):
    def detail(self):
        print("This book is convienent\n")

book1 = textBook()
book1.details()





class appliance:
    def __init__(self, watt):
        self.watt = watt
        print(f"The power of Fan is {self.watt}.")

class fan(appliance):
    def __init__(self, speed):
        self.speed = speed
        print(f"The speed of the Fan is {self.speed}.\n")

App = appliance("60W")
Fan = fan("High")




class animal:        
    def wild(self, types):
        self.types = types
        print(f"This animal is {self.types}")

class mammal(animal):
    def __init__(self):
        print("This is a Mammal")

class human(mammal):
    def __init__(self):
        print("This is a Human")


Human = human()
Human.wild("Warm-Blooded")

