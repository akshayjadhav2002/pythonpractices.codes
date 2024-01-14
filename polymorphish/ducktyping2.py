class Demo:
    def fun(self):
        print("IN demo :Fun")

class Memo:
    def gun(self):
        print("IN Memo :Gun")

def callFun (obj):
    if(hasattr(obj,"fun")): 
        #Ducktyping  :- checking the type of object at runtime is called as ducktyping
        obj.fun()
    else:
        obj.gun()

obj1 = Demo()
obj2 = Memo()

callFun(obj2)