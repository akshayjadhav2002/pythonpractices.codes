class Employ:
    z =10
    def __init__(self):
        print("In constructor")
        self.x =20
        self.y =30
    def disp(self):
        print(self.x)
        print(self.y)
    print(z)
obj = Employ()
obj.disp()