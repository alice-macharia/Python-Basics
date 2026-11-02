#inheritance

class Employee:
    def __init__(self, name, email, department, salary):
        self.name = name
        self.salary = salary
        self.email = email
        self.department = department

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class PermanentEmployee(Employee):  #inheriting
    def __init__(self, name, email, department, salary, cover, increment):
        super().__init__(name, email, department, salary)
        self.cover = cover
        self.increment = increment


class ContractEmployee(Employee):
    def __init__(self, name, email, department, salary, tenure):
        super().__init__(name, email, department, salary)
        self.tenure = tenure

    def show_details(self):
        print(f"Name, {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Tenure: {self.tenure}")



p1 = PermanentEmployee("Jane Mwa", "jm@yahoo", "HR", 100_000, 300, 300 )
c1 = ContractEmployee("Duke Dennis", "duke@gmail.com", "Sales", 80_000, 3)


p1.show_details()
c1.show_details()
