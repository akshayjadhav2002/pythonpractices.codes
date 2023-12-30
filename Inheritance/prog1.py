class demo:
    def __init__ (self):
        self.x =10
        self.y =20
    def setData(self):
        self.z=30
    def printData(self):
        print(self.x)
        print(self.y)
        print(self.z) #Error:-z is not visible to printData method
obj1 = demo() 
obj1.printData()
