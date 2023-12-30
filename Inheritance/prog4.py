class parent (object):
    def __init__(self):
        print("In constructor-1")
    def parentFun(self):
        print("In parent function")

class child (parent):
    def __init__(self):    #constructor is overriden and method is inheritend
        print("In constructor -2")

obj = child()
obj.parentFun()