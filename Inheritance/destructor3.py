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
 
obj1 = parent()
obj1 = parent()
print("code end")

"""
In constructor
In constructor 
In destructor 
//obj1 is deleted it notifies that object is goining to be deleted
code end
In destructor
"""