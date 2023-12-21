def decorFun(fun):
    def wrapper():
        print("Start wrapper")
        fun()
        print("End wrapper")
    return wrapper
#@decorFun
def normalFun():
    print("Hello in normal fun")

normalFun = decorFun(normalFun)
normalFun()
