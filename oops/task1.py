#an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.



from abc import ABC,abstractmethod
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    def __init__(self):
        self.name=input("enter the employee name:")
        self.age=int(input("enter the age:"))
        self.empid=int(input("enter the empid:"))

class Fulltimeemployee(Employee):

    def __init__(self):
        super().__init__()
        self.monthly_salary=int(input("enter the  monthly salary:"))

    def calculate_salary(self):
        print("total full time salary:",self.monthly_salary)

class Parttimeemployee(Employee):

    def __init__(self):
        super().__init__()
        self.rate=int(input("enter the rate:"))
        self.hours=int(input("enter the hour:"))

    def calculate_salary(self):
        print("total part time salary:", self.rate*self.hours)

e1=Fulltimeemployee()
e1.calculate_salary()

e2=Parttimeemployee()
e2.calculate_salary()