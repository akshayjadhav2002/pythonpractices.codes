class parent:
    def __init__(self,name):
        print("In const parent")
        self.name =name
    def Name(self):
        print(name)
    @classmethod
    def Info(cls):
        print(cls.name)

    @staticmethod
    def parinfo():
        print(obj.name)

class child(parent):
    pass
obj = child("Akshay")
child.parinfo()
