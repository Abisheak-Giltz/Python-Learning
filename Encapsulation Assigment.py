
# Encapsulation Assignment

class employee:
    def __init__(self, name, depart, salary):
        self.name = name
        self._depart = depart # protected variable
        self.__salary = salary # private variable

    def showDetails(self):
        print(f"Name\t\t:\t{self.name}")
        print(f"Department\t:\t{self._depart}")
        print(f"Salary\t\t:\t{self.__salary}\n")

employee1 = employee("Abisheak", "Python Developer", 45000)
employee1.showDetails()

employee2 = employee("Lord Aizen", "Backend Developer", 120000)
employee2.showDetails()





class animal:
    def __init__(self, name, types):
        self.name = name
        self._types = types

    def typeOfAnimal(self):
        print(f"Name : {self.name}")
        print(f"The type of Animal is {self._types}")

class dog(animal):
    def __init__(self, name, types, count):
        super().__init__(name, types)
        self.__count = count

dog1 = dog("Golden Retriver", "Mammal", 12)
dog1.typeOfAnimal()
