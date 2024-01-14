class parent:
    z = 30
    def __init__(self):
        print("In constructor")
        self.x=10
        self.y=20
    def dispData(self):
        print(self.x)
        print(self.y)
    
    @classmethod
    def dispParent(cls):
        print(cls.z)

    def __del__(self):
        print("In destructor")
 
obj = parent()
obj.dispParent()
obj.dispData()
#obj.__del__()          #It notifies that object is going to be deletedq