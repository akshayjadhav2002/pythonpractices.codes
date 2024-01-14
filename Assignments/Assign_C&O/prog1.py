class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def information(self):
        print("Name is :",self.name)
        print("Age is :" ,self.age)
    
name = input("Enter the Name")
age = int(input("Enter the Age"))

if __name__ == "__main__":
    obj1 = Human(name,age)
    obj1.information()