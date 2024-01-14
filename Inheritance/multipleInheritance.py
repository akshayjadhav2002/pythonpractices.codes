class parent:
    def dispData(self):
        print("In dispData")

class parent2:
    def printData(self):
        print("In printData")

class child(parent,parent2):
    pass

obj = child()
obj.dispData()
obj.printData()

print(child.mro())
