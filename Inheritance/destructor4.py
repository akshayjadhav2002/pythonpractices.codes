class parent:
    def __init__(self):
        print("In parent constructor")
        self.x=10
        self.y =20
    def dispParent(self):
        print(self.x)
        print(self.y)

class child (parent):
    def __init__ (self):  
        print("In child constructor")
        super().__init__()
        self.x = 30
        self.y = 40
        

obj = child()
obj.dispParent()

