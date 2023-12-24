# decorator chaining 

def decorFun(func):       # func--> address of wrapper1
    def wrapper():
        print("Start wrapper2")
        func()              #wrapper1()
        print("End Wrapper2")
    return wrapper
def decorRun(func): #func---> normalFun
    def wrapper():
        print("start wrapper1")
        func()                # normalFun()
        print("End Wrapper1")
    return wrapper

#@decorFun
#@decorRun
def normalFun():
    print("In normal fun")

#normalFun()

#internal implementation
#normalFun=decorFun(normalFun)
normalFun= decorFun(decorRun(normalFun))        #decorFun(addres of wrapper1) #normalFUn --->address of wrapper2
normalFun()