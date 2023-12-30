class parent (object):
    def __init__(self):
        print("In constructor-1")
    def parentFun(self):
        print("In parent function")

class child (parent):
    def __init__(self):    #constructor is overriden and method is inheritend
        #parent.__init__(self)
        #super().__init__()
        print(super().__init__()) #none
        print(parent.__init__(self)) #none
        print("In constructor -2")
    def childFun(self):
        print("In child fun")


obj = child()
obj.parentFun()
obj.childFun()