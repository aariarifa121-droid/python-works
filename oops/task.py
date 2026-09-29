class Hospital:
    def __init__(self):
        self.hos_name = input("Enter Hospital name: ")
        self.location = input("Enter location: ")
        self.phone = int(input("Enter Phone: "))

    def display_hospital(self):
        print("Hospital Name:", self.hos_name)
        print("Phone:", self.phone)
        print("Location:", self.location)


class Department:
    def __init__(self):
        self.department_name = input("Enter Department name: ")

    def display_department(self):
        print("Department:", self.department_name)


class Patient(Hospital, Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)

        self.patient_name = input("Enter Patient name: ")
        self.age = int(input("Enter Age: "))

    def full_summary(self):
        Hospital.display_hospital(self)
        Department.display_department(self)

        print("Patient Name:", self.patient_name)
        print("Age:", self.age)


p = Patient()
p.full_summary()