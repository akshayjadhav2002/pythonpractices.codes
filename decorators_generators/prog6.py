def decorFun(fun):      #fun-->normalFun

    def wrapper():
        print("Start wrapper")
        fun()               #-->calls the normalFun and print statement
        print("End wrapper")
    return wrapper   # returns the addres of wrapper

#@decorFun
def normalFun():
    print("Hello in normal fun")

normalFun = decorFun(normalFun)  ### Stores the address of the decorFun in normalFun 
                                ### this line is similar to the @decorfun[Decorator]
normalFun()                     #normalFun calls the -->wrapper() in decorFun()
