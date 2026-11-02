#bank account == owner, account, number, balance, history
from datetime import date, datetime


class Client:
    def __init__(self, name:str, kra_pin:str, dob:str, gender:str):
        self.name = name
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(self.name)
        print(self.kra_pin)
        print(self.dob)
        print(self.gender)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob, '%Y-%m-%d')
        age = today.year - birth_date.year
        return age

class BankAccount:
    def __init__(self, owner:Client, acc_no:str, balance:int):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount:int):
        self.balance += abs(amount)

    def withdraw(self, amount:int):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        print(self.owner.name)
        print(self.owner.gender)
        print(self.owner.kra_pin)
        print(self.acc_no)
        print(self.balance)
        print("-------------")


jane: Client = Client('jane', '123456', '1999-10-4', 'M')
ahmed = Client('ahmed', '123456', '2003-4-5', 'F')

# noinspection argument-list
acc1 = BankAccount(jane, '1111', 70_00)
acc2 = BankAccount(ahmed, '2222', 5000)
acc3 = BankAccount(jane, '3333', 6000)

acc1.deposit(10_000)
acc1.deposit(2000)
acc1.deposit(9000)


acc1.print_details()
acc1.withdraw(10_00)
acc1.print_details()


print("Jane Age", jane.calc_age())
print("Ahmed Age", ahmed.calc_age())


# print(acc1.owner.names.acc1.owner.calc_age())
# print(jane.name, jane.calc_age())


# dob = '2004-4-6' #yymmdd
#
# today = date.today()
# # print(f"{today.year}-{today.month}-{today.day}")
# #covert string to date
# birth_date = datetime.strptime(dob, '%Y-%m-%d')
# age = today.year - birth_date.year
# print(age)

# accurate_age =today - birth_date
# print(accurate_age)