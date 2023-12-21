class Demo:
    x =10     # class variable/static variable---> visible for class and objects
    def __init__(self): #constructor 

        self.y=20       #instance variable --> visible for only objects

    @classmethod
    def disp(cls):
        print(cls.x)
        print(Demo.x)
obj1=Demo()
obj1.disp()