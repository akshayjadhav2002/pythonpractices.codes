class parent (object):
    def __init__(self):
        print("In constructor-1")
    def parentFun(self):
        print("In parent function")

class child (parent):
    pass
obj = child()
obj.parentFun()