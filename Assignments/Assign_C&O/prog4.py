class parent:

    def __init__(self,Name,age):
        self.Name= Name
        self.age = age
    def parentInfo(self):
        print(Name)
        print(age)

class child(parent):
    childName = "akshay"
    def parentInfo(self):
        print(self.Name)
        print(self.age)
        print(self.childName)

obj = child("XyZ",20)
obj.parentInfo()

#XyZ
#20
#akshay