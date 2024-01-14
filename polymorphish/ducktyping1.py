class Demo:
    def fun(self):
        print("In Demo Fun")

class Memo:
    def fun(self):
        print("In Memo gun")

def callFun(obj): 
# here obj decide of which class object is at runtimeso it is call as dynamic binding and acts as polymorphism
    obj.fun()

obj1 = Demo()
obj2 = Memo()

callFun(obj2)