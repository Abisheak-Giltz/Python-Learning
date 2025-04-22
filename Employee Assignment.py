
# Company Data - Using Class

class employee:
    def employeeData(self, name, emID, salary):
        self.name = name
        self.emID = emID
        self.salary = salary

    def salaryData(self, percent):
        increamentSalary = self.salary * percent
        self.salary += increamentSalary
        return print(f"Hello! {self.name} your Salary is Increased by {percent}.\nCurrent Salary: {self.salary}")
        

employee1 = employee()
employee1.employeeData("Abisheak", 24680, 45000)
salaryPercent = input("Enter Your New Salary Percent : ")
percent = float(salaryPercent) / 100
employee1.salaryData(percent)

employee2 = employee()
employee2.employeeData("Co-Worker", 13579, 25000)
salaryPercent = input("Enter Your New salary Percent : ")
percent = float(salaryPercent) / 100
employee2.salaryData(percent)

