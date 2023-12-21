class Demo:
    x =10     # class variable/static variable
    def __init__(self): #constructor 
        self.y=20       #instance variable
    @classmethod
    def disp(cls):
        print(cls.x)
        print(Demo.x)
obj1=Demo()
obj1.disp()