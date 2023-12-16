class Company:
    CompName = "FaceBook"
    def __init__(self):
        print("In Constructor")
        self.empId =12
        self.empName = "Kanha"
    def CompInfo(self):
        print(self.empId)
        print(self.empName)
        print(self.CompName)
emp1 = Company()
emp1.CompInfo()