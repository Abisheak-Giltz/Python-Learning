
# Bank Account - Using Class

class bankAccount:
    def accountHolder(self, name, acNum):
        self.name = name
        self.acNum = acNum

    def balance(self, activity, amount):
        balance = 20000
        if(activity == "deposit"):
            balance += amount
            return print("Acc.Name\t:\t", self.name, "\nAcc.Number\t:\t", self.acNum), print(f"Acc.Balance\t:\t {balance}")
        elif(activity == "withdraw"):
            balance -= amount
            return print("Acc.Name\t:\t", self.name, "\nAcc.Number\t:\t", self.acNum), print(f"Acc.Balance\t:\t {balance}")
        elif(activity == "balance check" or activity == "balance"):
            return print("Acc.Name\t:\t", self.name, "\nAcc.Number\t:\t", self.acNum), print(f"Acc.Balance\t:\t {balance}")

myAccount = bankAccount()
myAccount.accountHolder("Abisheak", "1234567890")

activity = input("What do you want to do with your account? : ")
act = activity.lower()

amount = input("Enter Your Amount : ")
amt = int(amount)

myAccount.balance(act, amt)
