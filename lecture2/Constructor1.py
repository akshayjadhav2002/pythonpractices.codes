class Employee:
    def __init__(self,empId,empName):
        print("In constructor")
        self.empId = empId
        self.empName=empName
    def empInfo(self):
        print(self.empId)
        print(self.empName)
emp1 = Employee(10,"Akshay")
emp2 = Employee(20,"Ram")
emp1.empInfo() 
emp2.empInfo()
