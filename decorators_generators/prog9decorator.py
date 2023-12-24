def outerFun(fun):
    def innerFun(*args):
        print("start inner fun")
        val=fun(*args)
        print('end inner fun')
        return val 
    return innerFun

@outerFun
def normalFun(x,y):
    print("In normal Function")
    return x + y
    
outerFun(normalFun(10,20))

# internally this happens
"""normalFun= outerFun(normalFun)
normalFun(10,20)"""