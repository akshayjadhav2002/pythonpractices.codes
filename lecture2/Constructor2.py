class Company:
    CompName = "FaceBook"
    def __init__(self):
        print("In Constructor")
        self.empId =12
        self.empName = "Kanha"
    def CompInfo(self):
        print(self.empId)
        print(self.empName)
        print(self.CompName) # we have to write or access the golbal or class variable by the class or self 
        
emp1 = Company()
emp1.CompInfo()